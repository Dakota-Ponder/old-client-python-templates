# web scraper with pagination
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.example.com?page='


def scrape_page(page_number):
    """Scrape titles from a single page of the website."""
    response = requests.get(BASE_URL + str(page_number))
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all('h2')
    for title in titles:
        print(title.text)


# Scrape titles from the first 5 pages:
for page in range(1, 6):
    scrape_page(page)
