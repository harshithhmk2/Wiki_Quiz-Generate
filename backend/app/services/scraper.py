import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def scrape_wikipedia(url: str):
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").get_text(strip=True)

    paragraphs = soup.select("p")
    content = " ".join(
        p.get_text(strip=True)
        for p in paragraphs[:15]
        if p.get_text(strip=True)
    )

    sections = []
    for h2 in soup.find_all("h2"):
        span = h2.find("span", class_="mw-headline")
        if span:
            sections.append(span.get_text(strip=True))


    return {
        "title": title,
        "content": content,
        "sections": sections
    }
