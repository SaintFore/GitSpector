import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("git spector")


@mcp.tool()
def hello_user(name: str) -> str:
    """打招呼"""
    return f"good afternoon {name}"


@mcp.tool()
async def get_github_profile(username: str) -> str:
    """获取github基本信息"""
    url = f"https://api.github.com/users/{username}"

    async with httpx.AsyncClient() as client:
        headers = {"User-Agent": "GitSpector/1.0"}
        response = await client.get(url=url, headers=headers)

        if response.status_code != 200:
            return f"无法找到{username}"

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
async def list_repos(username: str, limit: int = 5) -> str:
    """
    列出用户公开的仓库列表，按更新时间排序。
    Args:
        username: GitHub 用户名
        limit: 返回仓库的最大数量 (默认 5 个)
    """
    url = f"https://api.github.com/users/{username}/repos?sort=updated"

    async with httpx.AsyncClient() as client:
        headers = {"User-Agent": "GitSpector/1.0"}
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

        return f"用户 {username} 的最近 {limit} 个仓库:\n" + "\n".join(repo_lines)


def main():
    mcp.run()


if __name__ == "__main__":
    main()
