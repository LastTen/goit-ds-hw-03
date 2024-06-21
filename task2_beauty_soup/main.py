from modules import save_data_json, authors_info, get_authors_links, quotes_info

url = "http://quotes.toscrape.com"
selector_author_link = ".author + a"
file_name_authors = "authors.json"
file_name_quotes = "quotes.json"


def make_author_json(filename, url):
    save_data_json(filename, authors_info(get_authors_links(url, selector_author_link)))


def make_quotes_json(filename, url):
    save_data_json(filename, quotes_info(url))


if __name__ == "__main__":
    make_author_json(file_name_authors, url)
    make_quotes_json(file_name_quotes, url)
