import requests
from bs4 import BeautifulSoup
import json



def save_data_json(file, data):
    """Save the json data to a file"""
    with open(
        file,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(data, f, indent=4)
        
def load_data_json(file):
    """Load the json data from a file"""
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    return soup

def page_generator(base_url):
        counter = 1
        while True:
            page_url = f"{base_url}/page/{counter}/"
            soup = get_soup(page_url)
            if not soup.select(".author + a"):
                break
            yield soup
            counter += 1


def get_authors_links(url, selector):
    authors_link = []
    for page in page_generator(url):
        quotes = page.select(selector)
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
def quotes_info(url):
    quotes_info_list = []
    for soup in page_generator(url):
            quotes = soup.select(".quote")
            for quote in quotes:
                tags = []
                tags_section = quote.find(class_="tags")
                if tags_section:
                    links = tags_section.find_all("a")
                    for link in links:
                        tags.append(link.get_text())
                quotes_info_list.append({"tags": tags,
                                         "author": quote.select_one(".author").text,
                                         "quote": quote.select_one(".text").text,
                                         })

    return quotes_info_list
                

if __name__ == "__main__":

    url = "http://quotes.toscrape.com"
    selector_author_link = ".author + a"
    file_name_authors = "authors.json"
    print(quotes_info(url))
    
    
    # for soup in page_generator(url):
    #     quotes = soup.select(".quote")
    #     for quote in quotes:
    #         print(quote.select_one(".author").text)
    #         print(quote.select_one(".text").text)
    #         tags_section = quote.find(class_="tags")
    #         if tags_section:
    #             links = tags_section.find_all("a")
    #             for link in links:
    #                 print(link.get_text())
            

