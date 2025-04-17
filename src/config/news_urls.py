"""
News URL Configuration Module

This module contains URLs for various news sources used for scraping or accessing 
political news content from different media outlets.
"""

# Dictionary mapping news source names to their political news section URLs
# These URLs serve as base endpoints for retrieving political news content
NEWS_URLS = {
     "CNN": "cnn.com/politics",      # CNN politics section
     "Fox": "foxnews.com/politics",  # Fox News politics section
     "AP": "apnews.com/politics"     # Associated Press politics section
}