from urllib.parse import unquote, urlparse
from bs4 import BeautifulSoup
import requests
from sys import argv
import mimetypes

def parse(
    page_content: str,
    base_url: str,
):
    soup: BeautifulSoup = BeautifulSoup(page_content, "html.parser")
    links: list = soup.find_all("a")
    if links and isinstance(links, list):
        for link in links:
            href: str = unquote(link.get("href"))
            (mime, _) = mimetypes.guess_type(href)
            if mime != None and mime.startswith("video/"):
                if href.startswith("/"):
                    print(f"https://{base_url}{href}")
                else:
                    print(f"{href}")


content = requests.get(
    url=argv[1],
)
parse(content.text, urlparse(argv[1]).netloc)
