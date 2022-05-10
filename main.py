import bs4
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from product import Product


def create_url(search, state, page):
    return 'https://{}.olx.com.br/?o={}&q={}'.format(state, page, search)

def read_pages(search, state, pages):
    for p in range(0, pages, +1):
        url = Request(create_url(search, state, p), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(url).read()
        soup = BeautifulSoup(webpage, 'html.parser')

        div_products = soup.find_all('div', class_='fnmrjs-1 gIEtsI')

        for div_product in div_products:
            prd = Product(div_product)
            print(prd.name)

read_pages(10)



