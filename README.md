# SerpScoop

This is a fun & basic implementation of an MCP server - Build a functional MCP server - Integrate with clients of your choice. 

# Prerequisites
- MCP SDK
- UV pkg manager

# Get Started
- Follow link to install UV and initialize an empty project: https://docs.astral.sh/uv/getting-started/installation/
- Run the server: uv run .\main.py - Server will start and accept connections

# Connecting to Clients
Edit config file of your client to add the MCP servers of your choice. 
<pre>{
  "mcpServers": {
        "serpscoop": {
        "command": "uv",
        "args": [
          "--directory",
          "path/to-your-/project-dir",
          "run",
          "main.py"
        ]
      }
  }
}
</pre>

# MCP Python SDK Documentation
https://github.com/modelcontextprotocol/python-sdk
