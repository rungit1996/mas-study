import json

from mcp.server.fastmcp import FastMCP

mcp = FastMCP()


@mcp.tool()
async def calculator(expression: str) -> str:
    """计算一个合法的 Python 数学表达式并返回结果

    Args:
        expression: 合法的 Python 数学表达式，如 "2+3*5" 或 "(10-4)/2"

    Returns:
        计算结果的字符串格式
    """
    try:
        result = eval(expression)
        return json.dumps({"result:": result})
    except Exception as e:
        return json.dumps({"result": f"数学表达式计算出错：{str(e)}"})


if __name__ == "__main__":
    # mcp.run(transport="streamable-http")
    mcp.run(transport="stdio")
