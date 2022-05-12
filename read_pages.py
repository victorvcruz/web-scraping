from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from database import insert
from product import Product


all_states = ['ac', 'es', 'pb', 'ro', 'al', 'go', 'pr', 'rr', 'ap', 'ma', 'pe', 'sc', 'am', 'mt', 'pi',
              'sp', 'ba', 'ms', 'rj', 'se', 'ce', 'mg', 'rn', 'to', 'pa', 'rs']


def create_url(search, state, page):
    return 'https://{}.olx.com.br/?o={}&q={}'.format(state, page, search)


def read_pages(search, pages, states):

    for page in range(1, pages+1, +1):

        for state in states:

            url = Request(create_url(search, state, page), headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(url).read()
            soup = BeautifulSoup(webpage, 'html.parser')
            div_products = soup.find_all('div', class_='fnmrjs-1 gIEtsI')

            for div_product in div_products:
                prd = Product(div_product, state)
                insert(prd)