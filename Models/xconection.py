import requests


# URL EXAMPLE --- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=snp&term=NC_012920.1%3Am.16069C%3ET


# Function to create the URL from the position, and polymorphism
def create_url_full(position, base, poly):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=snp&term=NC_012920.1%3Am."
    return url + position + base + "%3E" + poly


def create_url_position(position):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=snp&term=MT%3A"
    return url + position


def connection(url):
    response = requests.get(url)
    return response


def get_data(response):
    return response.text


def status_code(response):
    return response.status_code


def do_all(position):
    url = create_url_position(position)
    response = connection(url)
    data = get_data(response)
    return data
