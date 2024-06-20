from modules import save_data_json, authors_info, get_authors_links

url = "http://quotes.toscrape.com"


def make_author_json(filename, url):

    save_data_json(filename, authors_info(get_authors_links(url)))


if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
    make_author_json("authors_links.json", url)
