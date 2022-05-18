from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from database import ConnectionPostgreSQL
from product import Product
import config

database = ConnectionPostgreSQL()


def create_url(search, state, page, price_min, price_max, filter):
    return 'https://{}.olx.com.br/?o={}&pe={}&ps={}&q={}{}'.format(state, page, price_max, price_min, search.replace(" ", "%20"), filter)


def read_pages(search, page_start, page_end, states, price_min, price_max, filter):
    products_list = []
    for page in range(page_start, page_end + 1, +1):

        for state in states:

            url = Request(create_url(search, state, page, price_min, price_max, filter),
                          headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(url).read()
            soup = BeautifulSoup(webpage, 'html.parser')
            div_products = soup.find_all(config.div_type, class_=config.div_class)
            print(type(div_products))

            for div_product in div_products:
                prd = Product(div_product, state, search)
                database.insert_product(prd)
                products_list.append(prd)

    return products_list
