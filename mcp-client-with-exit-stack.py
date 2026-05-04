import asyncio
from contextlib import AsyncExitStack

from mcp import StdioServerParameters, stdio_client, ClientSession


async def main() -> None:
    # 1. 初始化 stdio 的服务器连接参数
    server_params = StdioServerParameters(
        command="uv",
        args=[
            "--directory",
            "/Users/ysz/YS/Code/demo/mas/mas-study",
            "run",
            "mcp-server-demo.py"
        ],
        env=None
    )

    # 2.0 初始化一个异步上下文管理器
    exit_stack = AsyncExitStack()

    try:
        # 2. 创建标准输入输出客户端
        transport = await exit_stack.enter_async_context(stdio_client(server_params))

        # 3. 获取写入和写出流
        stdio, write = transport

        # 4. 创建客户端会话上下文
        session = await exit_stack.enter_async_context(ClientSession(stdio, write))

        # 5. 初始化 MCP 服务器连接
        # noinspection DuplicatedCode
        await session.initialize()

        # 6. 获取工具列表信息
        list_tools_response = await session.list_tools()
        tools = list_tools_response.tools
        print("工具列表：", [tool.name for tool in tools])

        # 7. 调用指定的工具
        call_tool_response = await session.call_tool("calculator", {"expression": "100+200"})
        print("工具结果：", call_tool_response)
    finally:
        await exit_stack.aclose()


if __name__ == "__main__":
    asyncio.run(main())
