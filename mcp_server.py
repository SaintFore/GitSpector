from mcp.server.fastmcp import FastMCP

mcp = FastMCP("git spector")


@mcp.tool()
def hello_user(name: str) -> str:
    """打招呼"""
    return f"good afternoon {name}"


def main():
    mcp.run()


if __name__ == "__main__":
    main()
