from urllib.parse import unquote, urlparse
from bs4 import BeautifulSoup
import requests
from sys import argv


def parse(
    page_content: str,
    base_url: str,
):
    soup: BeautifulSoup = BeautifulSoup(page_content, "html.parser")
    links: list = soup.find_all("a")
    if links and isinstance(links, list):
        for link in links:
            href: str = unquote(link.get("href"))
            if href.endswith("mp4"):
                if href.startswith("/"):
                    print(f"https://{base_url}{href}")
                else:
                    print(f"{href}")


content = requests.get(
    url=argv[1],
)
parse(content.text, urlparse(argv[1]).netloc)
