from product import Product
import psycopg2
import config


class ConnectionPostgreSQL:

    def __init__(self):
        self.conn = psycopg2.connect(
            host=config.db_host,
            database=config.db_database,
            user=config.db_user,
            password=config.db_password,
            port=config.db_port)

        print("Database connected")

    def insert_product(self, product: Product):
        try:
            cur = self.conn.cursor()

            sql = """
                INSERT INTO public.database_olx(id,name, price, state, ddd, cep,image) 
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """

            cur.execute(sql,
                        (product.link, product.name, product.price, product.state, product.DDD, product.cep, product.image))
            self.conn.commit()
            cur.close()
        except (Exception, psycopg2.Error) as error:
            print(f"Failed to insert {product.link} into table", error)

