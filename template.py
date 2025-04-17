import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s", datefmt="%H:%M:%S")

# Define the directory and file structure
files_arr = [
    # Main application files
    "main.py",
    ".env",
    "README.md",
    
    # Source directory structure
    "src/__init__.py",
    
    # API module
    "src/api/__init__.py",
    "src/api/serp_client.py",
    
    # Config module
    "src/config/__init__.py",
    "src/config/constants.py",
    "src/config/news_urls.py",
    
    # Content module
    "src/content/__init__.py",
    "src/content/fetcher.py",
    
    # Exception handling
    "src/exceptions.py",
    
    # Services module
    "src/services/__init__.py",
    "src/services/news_service.py",
    
    # Tools module
    "src/tools/__init__.py",
    "src/tools/news_tools.py",
    
    # Tests directory
    "tests/__init__.py",
    "tests/test_api.py",
    "tests/test_content.py",
    "tests/test_services.py",
    
    # Scratch directory for experiments
    "scratch/scratch.ipynb",
]

# Create the directory and file structure
for fp in files_arr:
    fp = Path(fp)
    fileDir, filename = os.path.split(fp)
    
    if fileDir:
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Created directory: {fileDir}. File created: {filename}")
    
    if (not os.path.exists(fp)) or (os.path.getsize(fp) == 0):
        with open(fp, "w") as f:
            pass
            logging.info(f"Created file: {filename}")   
    else:
        logging.info(f"{filename} already exists.")