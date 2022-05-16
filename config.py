from flask.json import JSONEncoder
from product import Product


class ProductJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Product):
            return {
                'name': obj.name,
                'price': obj.price,
                'state': obj.state,
                'cep': obj.cep,
                'ddd': obj.DDD,
                'link': obj.link,
                'image': obj.image
            }
        return super(ProductJSONEncoder, self).default(obj)


db_host = "localhost"
db_database = "postgres"
db_user = "postgres"
db_password = "postgres"
db_port = "5432"

all_states = ["ac", "es", "pb", "ro", "al", "go", "pr", "rr", "ap", "ma", "pe", "sc", "am",
              "mt", "pi", "sp", "ba", "ms", "rj", "se", "ce", "mg", "rn", "to", "pa", "rs"]

filter_recent = '&sf=1'
filter_relevance = ''
filter_lowest = '&sp=2'

div_type = 'div'
div_class = 'sc-12rk7z2-0 bDLpyo'
name_type = 'h2'
name_class = 'kgl1mq-0 iYdPim sc-bdVaJa daxpJj'
name_class_none = 'kgl1mq-0 iYdPim sc-bdVaJa hYhJJh'
price_type = 'span'
price_class = 'm7nrfa-0 cjhQnm sc-bdVaJa cpfGxa'
cep_type = 'span'
cep_class = 'sc-1c3ysll-1 flPYFW sc-bdVaJa bxVNCd'
image_type = 'img'
image_class = 'sc-101cdir-0 cldTqT'
image_class_none = 'sc-101cdir-1 fwpxEI'
link_type = 'a'
link_class = 'sc-12rk7z2-1 kQcyga'
