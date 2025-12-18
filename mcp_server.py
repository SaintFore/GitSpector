import httpx
import sys
from mcp.server.fastmcp import FastMCP
import base64
from dotenv import load_dotenv
import os
import logging

mcp = FastMCP("git spector")
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

load_dotenv()
headers = {
    "User-Agent": "GitSpector/1.0",
    "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
}


# @mcp.tool()
# def hello_user(name: str) -> str:
#     """打招呼"""
#     return f"good afternoon {name}"


@mcp.tool()
async def get_github_profile(owner: str) -> str:
    """获取github基本信息"""
    url = f"https://api.github.com/users/{owner}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, headers=headers)

        if response.status_code != 200:
            return f"无法找到{owner}"

        data = response.json()

        return f"""
        用户概览: {data.get("login")}
        用户页地址: {data.get("html_url")}
        当前仓库数量: {data.get("public_repos")}
        公共仓库地址: {data.get("repos_url")}
        粉丝数: {data.get("followers")}
        账号创建时间: {data.get("created_at")}
        """


@mcp.tool()
async def list_repos(owner: str, limit: int = 5) -> str:
    """
    列出用户公开的仓库列表，按更新时间排序。
    Args:
        owner: GitHub 用户名
        limit: 返回仓库的最大数量 (默认 5 个)
    """
    url = f"https://api.github.com/users/{owner}/repos?sort=updated"

    async with httpx.AsyncClient() as client:
        # headers = {"User-Agent": "GitSpector/1.0"}
        resp = await client.get(url, headers=headers)

        if resp.status_code != 200:
            return f"Error: 无法获取仓库列表 (Status: {resp.status_code})"

        repos = resp.json()

        recent_repos = repos[:limit]

        repo_lines = []
        for repo in recent_repos:
            name = repo.get("name")
            stars = repo.get("stargazers_count")
            lang = repo.get("language") or "未知语言"
            url = repo.get("html_url")

            line = f"- [{name}] (★{stars}) {lang}: {url}"
            repo_lines.append(line)

        if not repo_lines:
            return "该用户没有公开仓库。"

        return f"用户 {owner} 的最近 {limit} 个仓库:\n" + "\n".join(repo_lines)


@mcp.tool()
async def read_file(owner: str, repo: str, path: str) -> str:
    """
    读取 GitHub 仓库中的单个文件内容。
    Args:
        owner: 仓库拥有者
        repo: 仓库名
        path: 文件路径
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    async with httpx.AsyncClient() as client:
        # headers = {"User-Agent": "GitSpector/1.0"}
        response = await client.get(url, headers=headers)

        if response.status_code != 200:
            return f"Error: 无法读取文件 {path} (Status: {response.status_code})"

        data = response.json()

        # GitHub API 返回的数据里，content 字段是被 base64 编码的
        encoded_content = data.get("content", "")
        encoding_type = data.get("encoding")
        logging.info(encoded_content)
        logging.info(encoding_type)

        if encoding_type != "base64":
            return "Error: 未知的文件编码格式"

        try:
            # 1. 解码 Base64 -> 得到 bytes
            decoded_bytes = base64.b64decode(encoded_content)

            # 2. 解码 bytes -> 得到 str (假设是 UTF-8 文本)
            # 如果是图片或二进制文件，这里会报错，所以要 try-except
            result_content = decoded_bytes.decode("utf-8")
            return result_content

        except UnicodeDecodeError:
            return "Error: 该文件似乎是二进制文件（如图片），无法以文本形式读取。"
        except Exception as e:
            return f"Error: 解析文件时发生错误: {str(e)}"


@mcp.tool()
async def star_repo(owner: str, repo: str) -> str:
    """
    给指定的 GitHub 仓库点赞 (Star)。
    Args:
        owner: 仓库拥有者
        repo: 仓库名
    """
    url = f"https://api.github.com/user/starred/{owner}/{repo}"

    async with httpx.AsyncClient() as client:
        response = await client.put(url, headers=headers)
        # 204 代表成功，且没有返回内容
        logging.info(response.status_code)
        if response.status_code == 204:
            return f"成功：已给 {owner}/{repo} 点赞！🌟"
        elif response.status_code == 304:
            return f"提示：你已经给 {owner}/{repo} 点过赞了。"
        elif response.status_code == 401:
            return "错误：权限不足。请检查你的 Token 是否勾选了 'public_repo' 权限。"
        elif response.status_code == 404:
            return f"错误：找不到仓库 {owner}/{repo}。"
        else:
            return f"错误：操作失败 (Status: {response.status_code})"


@mcp.tool()
async def unstar_repo(owner: str, repo: str) -> str:
    """
    给指定的 GitHub 仓库取消点赞 (Unstar)。
    Args:
        owner: 仓库拥有者
        repo: 仓库名
    """
    url = f"https://api.github.com/user/starred/{owner}/{repo}"

    async with httpx.AsyncClient() as client:
        response = await client.delete(url, headers=headers)

        # 204 代表成功，且没有返回内容
        logging.info(response.status_code)
        if response.status_code == 204:
            return f"成功：已给 {owner}/{repo} 取消点赞！🌟"
        elif response.status_code == 304:
            return f"提示：你还未给 {owner}/{repo} 点过赞。"
        elif response.status_code == 401:
            return "错误：权限不足。请检查你的 Token 是否勾选了 'public_repo' 权限。"
        elif response.status_code == 404:
            return f"错误：找不到仓库 {owner}/{repo}。"
        else:
            return f"错误：操作失败 (Status: {response.status_code})"


def main():
    mcp.run()


if __name__ == "__main__":
    main()
