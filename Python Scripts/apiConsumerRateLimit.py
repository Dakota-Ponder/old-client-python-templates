# program that consumes an API that has a rate limit of 1 request per minute.
import requests
import time

BASE_URL = 'https://api.example.com/data?page='


def fetch_data(page_number):
    """Fetch data from the API, respecting rate limits."""
    response = requests.get(BASE_URL + str(page_number))
    if response.status_code == 429:  # Rate limit exceeded
        time.sleep(60)  # Wait for a minute and retry
        return fetch_data(page_number)
    return response.json()


# Fetch data from the first 5 pages:
for page in range(1, 6):
    data = fetch_data(page)
    print(data)
