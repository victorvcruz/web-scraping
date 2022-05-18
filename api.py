from flask import Flask, request, jsonify

from config import ProductJSONEncoder, all_states
from filters import Filter
from read_pages import read_pages
from request_api import RequestApi

app = Flask(__name__)
app.json_encoder = ProductJSONEncoder


@app.route('/products', methods=["POST", "GET"])
def products():
    request_api = RequestApi(request)

    return jsonify(
        read_pages(request_api.search, int(request_api.page_start), int(request_api.page_end), request_api.states,
                   request_api.price_min, request_api.price_max, Filter[request_api.filter].value))
