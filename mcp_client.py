import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run_client():
    server_params = StdioServerParameters(
        command="python", args=["mcp_server.py"], env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            # print(tools)
            # print(type(tools))  # mcp.types.ListToolsResult
            print(f"发现工具: {[tool.name for tool in tools.tools]}")

            result = await session.call_tool(
                "read_file",
                arguments={
                    "username": "SaintFore",
                    "repo": "CoinWatcher",
                    "path": "README.md",
                },
            )
            # print(type(result))
            # print(result)  # meta content是TextContent的list, structuredContent是dict, isError
            sr = result.structuredContent or {}
            print(f"result: {sr.get("result")}")


if __name__ == "__main__":
    asyncio.run(run_client())
