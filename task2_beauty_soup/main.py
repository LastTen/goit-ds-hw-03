from modules import (
    save_data_json,
    authors_info,
    get_authors_links,
    quotes_info,
    load_data_json,
)
from connect import db

url = "http://quotes.toscrape.com"
selector_author_link = ".author + a"
file_name_authors = "authors.json"
file_name_quotes = "quotes.json"


def make_author_json(filename, url):
    save_data_json(filename, authors_info(get_authors_links(url, selector_author_link)))


def make_quotes_json(filename, url):
    save_data_json(filename, quotes_info(url))


def insert_authors_to_db(filename):
    db.authors.insert_many(load_data_json(filename))
    print("Added authors")


def insert_quotes_to_db(filename):
    db.quotes.insert_many(load_data_json(filename))
    print("Added quotes")


if __name__ == "__main__":
    # make_author_json(file_name_authors, url)
    # make_quotes_json(file_name_quotes, url)
    # print(load_data_json(file_name_quotes))
    insert_authors_to_db(file_name_authors)
    insert_quotes_to_db(file_name_quotes)
