from mcp.server.fastmcp import FastMCP
from typing import Union

mcp=FastMCP("Math")

@mcp.tool()
def add(a: Union[int, str], b: Union[int, str]) -> int:
    """Add two numbers together."""
    return int(a) + int(b)

@mcp.tool()
def multiply(a: Union[int, str], b: Union[int, str]) -> int:
    """Multiply two numbers together."""
    return int(a) * int(b)

if __name__=="__main__":
    mcp.run(transport="stdio")
