# install pip install requests beautifulsoup4
# haven't used this yet due to not wanting my IP address to be blocked

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.example-jobsite.com/search?q=junior+developer'


def fetch_job_postings(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # These selectors are hypothetical and will differ for each website
    job_elements = soup.select('.job-listing')

    jobs = []
    for job_el in job_elements:
        title = job_el.select_one('.job-title').text
        company = job_el.select_one('.company-name').text
        location = job_el.select_one('.job-location').text

        job = {
            "title": title,
            "company": company,
            "location": location
        }
        jobs.append(job)

    return jobs


if __name__ == '__main__':
    job_postings = fetch_job_postings(BASE_URL)
    for job in job_postings:
        print(job)
