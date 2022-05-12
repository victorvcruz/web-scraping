from bs4.element import Tag


class Product:

    def __init__(self, div: Tag, state):
        self.name = div.find('h2', class_='sc-1iuc9a2-1 dTvKuJ sc-ifAKCX eKQLlb').get_text().strip()

        div_price = div.find('p', class_='sc-1iuc9a2-8 bTklot sc-ifAKCX eoKYee')
        if div_price is None:
            self.price = '0'
        else:
            self.price = div_price.get_text().replace("R$", "").replace(".", "").strip()

        div_cep = div.find('span', class_='sc-7l84qu-1 ciykCV sc-ifAKCX dpURtf').get_text().strip()
        divisor_ddd = div_cep.split(" - DDD ")
        self.cep = divisor_ddd[0]
        self.DDD = divisor_ddd[1]
        self.state = state.upper()
