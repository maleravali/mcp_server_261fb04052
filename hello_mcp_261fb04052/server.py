
from mcp.server.mcpserver import MCPServer

# Create an MCP server
mcp = MCPServer("Hello MCP")


# Tool 1: Get Greeting
@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for a student."""
    return f"Hello, {name}! Your first MCP tool works."


# Tool 2: Add Numbers
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# Run the MCP server
if __name__ == "__main__":
    mcp.run()
