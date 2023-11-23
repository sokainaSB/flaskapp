# buttonrunscript.py
import requests
from bs4 import BeautifulSoup

def fetch_page_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content and extract the page title
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"

        return title
    except requests.RequestException as e:
        return f"Error fetching page title: {e}"

def main(url):
    print("Script started")

    print(f"URL: {url}")

    page_title = fetch_page_title(url)
    print(f"Page Title: {page_title}")

    return page_title

if __name__ == "__main__":
    # Test the script independently
    default_url = "https://www.example.com"
    main(default_url)
