from typing import Optional, Dict
from mcp.server.fastmcp import FastMCP
from ..services.news_service import NewsService

class NewsTools:
    def __init__(self, mcp_instance: FastMCP):
        """
        Initialize NewsTools with a FastMCP instance.
        
        Args:
            mcp_instance: The FastMCP instance to register tools with
        """

        self.mcp = mcp_instance
        self.news_service = NewsService()
        self._register_tools()
    
    def _register_tools(self):
        """
        Register all news-related tools with the FastMCP instance.
        
        This method uses decorators to register functions as tools that can be
        called by agents or other components through the MCP framework.
        """
        
        @self.mcp.tool()
        async def get_news(query: str, website: str) -> Optional[Dict[str, str]]:
            """
            Search for relevant political news articles for a given query and website specified.
            Supports CNN, Fox News, and AP news.
            Only returns articles categorized under politics.
            
            Args:
                query: The query to search for (eg., "US-China trade war", "tariffs", "Supreme Court ruling immigration", "donald Trump")
                website: The website to search in (Eg., CNN, Fox News, AP News)
            """
            
            return await self.news_service.search_news_by_website(query, website)