from modules import save_data_json, authors_info, get_authors_links


def make_author_json(filename):
    save_data_json(filename, authors_info(get_authors_links()))


if __name__ == "__main__":
    make_author_json("authors_links.json")
