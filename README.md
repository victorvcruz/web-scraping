# This project is a web scraping in python that searches the [Olx](https://www.olx.com.br/)

To run project you need Python, Pip, [Docker](https://docs.docker.com/engine/install/) and [Docker-compose](https://docs.docker.com/compose/install/),  installed in your pc

## How to run project

1. run `sudo docker-compose up -d` in root directory
2. install missing dependencies of python
3. run main.py 
4. in http://127.0.0.1:5000/products insert your request
5. your requisition was made in database: 'database_olx'
6. for graphical analysis go to http://localhost:3000/dashboard/1-projetoeasy
7. place email: metabase@metabase.com and password: metabase0

To stop execution run `sudo docker-compose down`

### Application of the requisition

* query parameters:
```
search= (your search on olx)

page_start= (first page to be read)

page_end= (last page to be read)

price_min= (price min to your search)

price_max= (price max to your search)

filter= (default filter in olx: MOST_RECENT, RELEVANCE, LOWEST_PRICE
```

* example:

```http://127.0.0.1:5000/products?search=iphone&page_start=1&page_end=1&price_min=100&price_max=200&filter=RELEVANCE```

* JSON parameter
```
{
	"states" : (list of search states)
}
```
* example
```
{
	"states" : ["go", "sp", "rj"]
}
```
