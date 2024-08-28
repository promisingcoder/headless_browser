import requests
from bs4 import BeautifulSoup
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG)

query = '"Med Spa Owner" OR "Medical Spa Owner" OR "Med Spa Founder" OR "Medical Spa Founder" OR "Med Spa CEO" OR "Medical Spa CEO" ("United States" OR USA OR "New York" OR "California" OR "Texas" OR "Florida") -inurl:"posts" -inurl:"blog" site:linkedin.com/in/'
url = "https://searx.tiekoetter.com/search"

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

def search(url, query, pageno):
    logging.debug('Searching for query "%s" on page %s', query, pageno)

    params = {
        'q': query,
        'category_general': '1',
        'language': 'en-US',
        'time_range': '',
        'safesearch': '0',
        'theme': 'simple',
        'pageno': pageno
    }
    logging.debug('Making request to %s with headers %s and params %s', url, headers, params)

    try:
        session = requests.Session()
        response = session.get(url, params=params, headers=headers)
        logging.debug('Got response status code %s', response.status_code)
        logging.debug('Response content length: %d', len(response.content))

        if response.status_code != 200:
            logging.error('Received non-200 HTTP status code')
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        all_the_links = soup.find_all("a", attrs={"rel": "noreferrer"})

        logging.debug('Number of links found: %d', len(all_the_links))
        return all_the_links

    except Exception as e:
        logging.error('An error occurred: %s', e)
        return []

def save_links_to_file(links, filename="links.txt"):
    logging.debug('Saving %d links to file: %s', len(links), filename)
    try:
        with open(filename, 'w') as file:
            for link in links:
                file.write(link + "\n")
        logging.debug('Successfully saved links to %s', filename)
    except Exception as e:
        logging.error('An error occurred while saving links to file: %s', e)

results = set()
n = 1

while True:
    logging.debug('Starting search on page %d', n)
    new_results = search(url, query, n)
    
    if not new_results:
        logging.debug('No new results found, breaking loop')
        break

    # Filter out duplicates and add new results to the set
    unique_results = {link.get("href") for link in new_results if link.get("href") not in results}
    logging.debug('Number of unique new results: %d', len(unique_results))

    if not unique_results:
        logging.debug('No unique new results, breaking loop')
        break

    results.update(unique_results)

    time.sleep(random.uniform(2, 5))
    n += 1

logging.debug('Total unique results found: %d', len(results))

# Save the unique results to a text file
save_links_to_file(results,filename="links2.txt")
