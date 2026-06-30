"""
SaiKet Systems - Python Development Internship
Task 4: Basic Web Scraper

Description:
Scrapes news headlines from a website using requests and BeautifulSoup,
and displays them to the user in a readable format. Includes error
handling for network and parsing issues.

Skills demonstrated: Web Scraping Libraries (BeautifulSoup, Requests),
HTML Parsing Basics, Data Extraction Techniques

NOTE: Run `pip install requests beautifulsoup4` before executing this
script if those packages are not already installed.
"""

import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
        )
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the website. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred - {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error: An unexpected request error occurred - {e}")
    return None


def extract_headlines(html, tag="h2", limit=10):
    """
    Extracts text from the given HTML tag (commonly used for headlines).
    Adjust `tag` and CSS selectors based on the target website's structure.
    """
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.find_all(tag)

    headlines = []
    for el in elements:
        text = el.get_text(strip=True)
        if text:
            headlines.append(text)
        if len(headlines) >= limit:
            break

    return headlines


def display_headlines(headlines):
    if not headlines:
        print("No headlines were found. The page structure may have changed,")
        print("or you may need to update the HTML tag used for extraction.")
        return

    print("\n===== LATEST HEADLINES =====")
    for i, headline in enumerate(headlines, start=1):
        print(f"{i}. {headline}")
    print("=============================\n")


def main():
    print("===== BASIC WEB SCRAPER =====")
    url = input("Enter the URL of the news website to scrape: ").strip()

    if not url:
        print("URL cannot be empty.")
        return

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    html = fetch_page(url)
    if html is None:
        return

    # Default tag is 'h2' since many news sites use it for headlines.
    # Change this (e.g., to 'h1', 'h3', or a specific class) depending on the target site.
    tag = input("Enter the HTML tag for headlines (press Enter for default 'h2'): ").strip() or "h2"

    headlines = extract_headlines(html, tag=tag, limit=10)
    display_headlines(headlines)


if __name__ == "__main__":
    main()
