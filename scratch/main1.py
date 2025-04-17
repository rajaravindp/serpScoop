import os
import httpx
import json

from bs4 import BeautifulSoup as bs4
from typing import Optional, Dict

from config.news_urls import NEWS_URLS
from src.exceptions import EXCEPTION_HANDLERS
from config.constants import USER_AGENT, SERP_SEARCH_URL

from mcp.server.fastmcp import FastMCP

from dotenv import load_dotenv

load_dotenv()


mcp = FastMCP("mcp-pilot")

async def search_news(query: str, location: Optional[str] = None) -> Optional[dict]:
    """
    Perform a news search using the SERP API.

    Args:
        query (str): The search query.
        location (str): The location for the news search.

    Returns:
        dict | None: The search results as a dictionary or None if an error occurs.
    """

    
    if not os.getenv("SERP_API_KEY"):
        raise ValueError("Please set the SERP_API_KEY environment variable.")
    
    
    headers = {
        "X-API-KEY": os.getenv("SERP_API_KEY"),
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
    }

    
    params = {
        "q" : query, 
        "tbm" : "nws", 
        "hl" : "en", 
        "sort_by" : "most_recent",
        "safe" : "active"
    }
    
    if location is not None:
        params["location"] = location

    
    payload = json.dumps(params)

    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(SERP_SEARCH_URL, headers=headers, data=payload, timeout=20.0)
            response.raise_for_status()  
            return response.json()
    except tuple(EXCEPTION_HANDLERS.keys()) as e: 
        print(EXCEPTION_HANDLERS[type(e)], f": {e}")

async def get_news_url(url: str) -> Optional[dict]:
    """
    Get news URLs.

    Args:
        url (str): The URL to fetch.

    Returns:
        Optional[dict]: The parsed news content or None if an error occurs.
    """
    
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=20.0)
            response.raise_for_status()  
            soup = bs4(response.text, "html.parser")
            text = soup.get_text()
            return text
    except tuple(EXCEPTION_HANDLERS.keys()) as e: 
        print(EXCEPTION_HANDLERS[type(e)], f": {e}")

@mcp.tool()  
async def get_news(query: str, website: str) -> Optional[Dict[str, str]]:
    """
    Search for relevant political news articles for a given query and website specified. 
    Supports CNN, Fox News, and AP news. 
    Only returns articles categorized under politics.

    Args:
        query: The query to search for (eg., "US-China trade war", "tariffs", "Supreme Court ruling immigration", "donald Trump")
        website: The website to search in (Eg., CNN, Fox News, AP News) 
    """

    if website not in NEWS_URLS:
        raise ValueError(f"Website '{website}' is not in the list of allowed news URLs.")
    
    query = f"site:{NEWS_URLS[website]} {query}"
    results = await search_news(query)
    if len(results["organic"]) == 0:
        return "No results"
    res_txt = str()
    for res in results['organic']:
        res_txt += await get_news_url(res['link'])
    return res_txt

if __name__ == "__main__":
    mcp.run(transport="stdio")