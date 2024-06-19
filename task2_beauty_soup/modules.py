import requests
from bs4 import BeautifulSoup
import json
import os

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

def save_data_json(file, data):
    """Save the json data to a file"""
    with open(
        file,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(data, f, indent=4)

def get_authors_links():
    authors_link = []
    quotes = soup.select(".author + a")
    for quote in quotes:
        link = f"{url}{quote["href"]}"
        if link not in authors_link:
            authors_link.append(f"{url}{quote["href"]}")
    return authors_link

def authors_info(authors):
    data = []
    for author in authors:
        link = requests.get(author)
        soup = BeautifulSoup(link.text, "lxml")
        data.append({'fullname': soup.select_one(".author-title").text, 
                'born_date': soup.select_one(".author-born-date").text,
                'born_location': soup.select_one(".author-born-location").text,
                'description': soup.select_one(".author-description").text,
                })
    return data

if __name__ == "__main__":
    # save_data_json('file.json', authors_info(get_authors_links()))
    # authors_info(get_authors_links())
    print(get_authors_links())
    # print(soup)
