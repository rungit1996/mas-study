import subprocess

from mcp.server import FastMCP

mcp = FastMCP()


@mcp.tool()
async def bash(command: str) -> dict:
    """传递 command 命令，在 MAC 下执行 CMD 命令

    Args:
        command: 需要执行的 command 命令

    Returns:
        返回命令的执行状态、结果、错误信息
    """
    result = subprocess.run(
        command,
        shell=True,  # 让命令行通过 cmd 执行
        capture_output=True,  # 捕获输出
        text=True,  # 输出解码为字符串
    )

    return {
        "return-code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
