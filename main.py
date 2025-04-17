import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from src.tools.news_tools import NewsTools
import sys

# Initialize MCP server
mcp = FastMCP("serpscoop")

def main():
    try:
        # Load environment variables
        load_dotenv()
        # Register tools
        news_tools = NewsTools(mcp)
        # Run the server
        mcp.run(transport="stdio")
    except Exception as e:
        # Log the exception to stderr
        print(f"Server error: {e}", file=sys.stderr)
        raise 

if __name__ == "__main__":
    main()
