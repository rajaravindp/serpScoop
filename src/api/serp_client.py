import os
import httpx
import json
from typing import Optional, Dict
from ..exceptions import EXCEPTION_HANDLERS
from ..config.constants import USER_AGENT, SERP_SEARCH_URL

class SerpApiClient:
    """
    A client for interacting with the SERP API to perform search operations.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the SerpApiClient with an API key.

        Args:
            api_key (Optional[str]): The API key for authenticating with the SERP API.
                                     If not provided, it will attempt to fetch from the
                                     SERP_API_KEY environment variable.

        Raises:
            ValueError: If no API key is provided or found in the environment variables.
        """
        self.api_key = api_key or os.getenv("SERP_API_KEY")
        if not self.api_key:
            raise ValueError("Please set the SERP_API_KEY environment variable.")
        
        # Set up headers for API requests
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        }
    
    async def search_news(self, query: str, location: Optional[str] = None) -> Optional[Dict]:
        """
        Perform a news search using the SERP API.

        Args:
            query (str): The search query string.
            location (Optional[str]): The location to refine the search results (optional).

        Returns:
            Optional[Dict]: The JSON response from the API if successful, or None if an error occurs.
        """
        # Define the search parameters
        params = {
            "q": query,  # Search query
            "tbm": "nws",  # Search type: news
            "hl": "en",  # Language: English
            "sort_by": "most_recent",  # Sort by most recent
            "safe": "active"  # Enable safe search
        }
        
        if location is not None:
            params["location"] = location  # Add location to payload params if provided
            
        payload = json.dumps(params)  # Convert parameters to JSON payload
        
        try:
            # Make an asynchronous POST request to the SERP API
            async with httpx.AsyncClient() as client:
                response = await client.post(SERP_SEARCH_URL, headers=self.headers, data=payload, timeout=20.0)
                response.raise_for_status()  # Raise an exception for HTTP errors
                return response.json()  # Return the JSON response
        except tuple(EXCEPTION_HANDLERS.keys()) as e:
            # Handle exceptions using predefined handlers
            print(EXCEPTION_HANDLERS[type(e)], f": {e}")
            return None