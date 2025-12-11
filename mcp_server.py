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


def main():
    mcp.run()


if __name__ == "__main__":
    main()
