from bs4.element import Tag
import config


class Product:

    def __init__(self, div: Tag, state):
        div_name = div.find(config.name_type, class_=config.name_class)
        if div_name is None:
            self.name = div.find(config.name_type, class_=config.name_class_none).get_text().strip()
        else:
            self.name = div_name.get_text().strip()

        div_price = div.find(config.price_type, class_=config.price_class).get_text()
        if div_price == '':
            self.price = '0'
        else:
            self.price = div_price.replace("R$", "").replace(".", "").strip()

        div_cep = div.find(config.cep_type, class_=config.cep_class).get_text().strip()
        divisor_ddd = div_cep.split(" - DDD ")
        self.cep = divisor_ddd[0]
        self.DDD = divisor_ddd[1]
        self.state = state.upper()

        div_image = div.find(config.image_type, class_=config.image_class)
        if div_image is None:
            div_image = div.find(config.image_type, class_=config.image_class_none)
        self.image = div_image['src']

        self.link = div.find(config.link_type, class_=config.link_class)['href']


