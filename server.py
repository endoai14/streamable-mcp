from mcp.server.fastmcp import FastMCP 

mcp = FastMCP(name='server',
              host='0.0.0.0')

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hello, {name}!"



if __name__ == "__main__":
    mcp.run(transport='streamable-http')