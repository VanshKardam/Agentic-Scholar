from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query : str) -> str:
    """
    Use this tool to search the web for latest information relevant to the query and return Titles, URLs and Snippets for the top 3 results.
    """
    results = tavily.search(query = query, max_results = 3)
    
    out = []

    for r in results["results"]:
        out.append(
            f"Title : {r['title']}\n"
            f"URL : {r['url']}\n"
            f"Snippet : {r['content'][:300]}\n"
        )

    return "\n---\n".join(out)

@tool
def scrape_url(url: str) -> str:
    """
    Scrape and return clean text content from a given URL for deeper reading.
    """
    try:
        resp = requests.get(url, timeout=10, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(['script', 'style', 'header', 'footer', 'nav']):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL : {str(e)}"