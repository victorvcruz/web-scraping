from flask import Flask, request, jsonify
from config import ProductJSONEncoder
from filters import Filter
from read_pages import read_pages

app = Flask(__name__)
app.json_encoder = ProductJSONEncoder


@app.route('/products', methods=["POST", "GET"])
def products():
    input_json = request.get_json(force=False, silent=True)

    args = request.args
    search = args.get("search")
    page_start = args.get("page_start")
    page_end = args.get("page_end")
    price_min = args.get("price_min")
    price_max = args.get("price_max")
    filter = args.get("filter")
    states = input_json['states']

    return jsonify(
        read_pages(search, int(page_start), int(page_end), states, price_min, price_max, Filter[filter].value))