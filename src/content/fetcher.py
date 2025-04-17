import httpx
from bs4 import BeautifulSoup as bs4
from typing import Optional
from ..exceptions import EXCEPTION_HANDLERS

class ContentFetcher:
    """
    A utility class for fetching content from web URLs.
    
    This class provides static methods to retrieve and parse web content
    using asynchronous HTTP requests with error handling.
    """
    
    @staticmethod
    async def fetch_url_content(url: str) -> Optional[str]:
        """
        Asynchronously fetches and parses content from a specified URL.
        
        Args:
            url (str): The URL to fetch content from
            
        Returns:
            Optional[str]: The parsed text content of the URL, or None if the request failed
            
        Raises:
            Various exceptions handled by EXCEPTION_HANDLERS
        """
        try:
            # Create an async HTTP client with a context manager to ensure proper cleanup
            async with httpx.AsyncClient() as client:
                # Send GET request with a timeout to prevent hanging
                response = await client.get(url, timeout=20.0)
                # Raise an exception for bad status codes (4xx, 5xx)
                response.raise_for_status()
                # Parse the HTML content using BeautifulSoup
                soup = bs4(response.text, "html.parser")
                # Extract and return only the text content
                return soup.get_text()
        except tuple(EXCEPTION_HANDLERS.keys()) as e:
            # Handle known exceptions using predefined error messages
            print(EXCEPTION_HANDLERS[type(e)], f": {e}")
            return None