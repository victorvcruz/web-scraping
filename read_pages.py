from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

import config
from database import insert
from product import Product


all_states = ['ac', 'es', 'pb', 'ro', 'al', 'go', 'pr', 'rr', 'ap', 'ma', 'pe', 'sc', 'am', 'mt', 'pi',
              'sp', 'ba', 'ms', 'rj', 'se', 'ce', 'mg', 'rn', 'to', 'pa', 'rs']


def create_url(search, state, page):
    return 'https://{}.olx.com.br/?o={}&q={}'.format(state, page, search)


def read_pages(search, page_start, page_end, states):

    for page in range(page_start, page_end+1, +1):

        for state in states:

            url = Request(create_url(search, state, page), headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(url).read()
            soup = BeautifulSoup(webpage, 'html.parser')
            div_products = soup.find_all(config.div_type, class_=config.div_class)

            for div_product in div_products:
                prd = Product(div_product, state)
                print(prd.state)