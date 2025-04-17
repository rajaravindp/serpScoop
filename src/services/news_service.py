from typing import Optional, Dict, List
from ..api.serp_client import SerpApiClient
from ..content.fetcher import ContentFetcher
from ..config.news_urls import NEWS_URLS

class NewsService:
    """
    Service class for news-related operations.
    
    This class handles searching for news articles on specific websites
    and retrieving their content using the SERP API and content fetcher.
    """
    
    def __init__(self):
        """
        Initialize the NewsService with required API client and content fetcher.
        """
        self.api_client = SerpApiClient()
        self.content_fetcher = ContentFetcher()
    
    async def search_news_by_website(self, query: str, website: str) -> Optional[str]:
        """
        Search for news articles on a specific website and retrieve their content.
        
        Args:
            query (str): The search query to find relevant news articles
            website (str): The news website to search (must be one of the predefined sites)
            
        Returns:
            Optional[str]: Combined content from all found articles or error message
            
        Raises:
            ValueError: If the specified website is not in the allowed list
        """

        if not website:
            website = "AP news"

        # Validate that the requested website is in our allowed list
        if website not in NEWS_URLS:
            raise ValueError(f"Website '{website}' is not in the list of allowed news URLs.")
        
        # Create a site-specific search query using the website's URL
        site_query = f"site:{NEWS_URLS[website]} {query}"
        # Perform the search using the SERP API client
        results = await self.api_client.search_news(site_query)
        
        # Check if we have valid results
        if not results or "organic" not in results or len(results["organic"]) == 0:
            return "No results found"
        
        # Fetch and combine content from each URL
        all_content = []
        for result in results['organic']:
            # Fetch the content for each search result link
            content = await self.content_fetcher.fetch_url_content(result['link'])
            if content:
                all_content.append(content)
        
        # Join all fetched content with double newlines or return error message if none was retrieved
        return "\n\n".join(all_content) if all_content else "Failed to fetch content"