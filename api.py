from flask import Flask, request, jsonify

from config import ProductJSONEncoder, all_states
from filters import Filter
from read_pages import read_pages

app = Flask(__name__)
app.json_encoder = ProductJSONEncoder


@app.route('/products', methods=["POST", "GET"])
def products():
    input_json = request.get_json(force=False, silent=True)

    try:
        states = input_json['states']
        for state in states:
            if state not in all_states:
                return jsonify({'message': f"State {state} not found"}), 400
    except TypeError:
        states = all_states

    args = request.args
    search = args.get("search")
    page_start = args.get("page_start", None)

    if page_start is None:
        page_start = 0
    try:
        int(page_start)
    except ValueError:
        return jsonify({'message': f"Page Start {page_start} not is a number"}), 400

    page_end = args.get("page_end", None)
    if page_end is None:
        page_end = 0
    try:
        int(page_end)
    except ValueError:
        return jsonify({'message': f"Page End {page_end} not is a number"}), 400

    price_min = args.get("price_min", None)
    if price_min is None:
        price_min = ''

    price_max = args.get("price_max", None)
    if price_max is None:
        price_max = ''

    filter = args.get("filter", None)
    if filter is None:
        filter = 'RELEVANCE'
    if filter not in [Filter.MOST_RECENT.name, Filter.LOWEST_PRICE.name, Filter.RELEVANCE.name]:
        return jsonify({'message': f"Filter {filter} not found"}), 400

    return jsonify(
        read_pages(search, int(page_start), int(page_end), states, price_min, price_max, Filter[filter].value))