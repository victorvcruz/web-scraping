from flask import Flask, jsonify, Request
from config import ProductJSONEncoder, all_states
from filters import Filter


class RequestApi():

    def validate_page(self, page):
        if not isinstance(page, int):
            return jsonify({'message': f"Page {page} not found"}), 400

    def validate_price(self, price):
        if not isinstance(price, int):
            return jsonify({'message': f"Price {price} not found"}), 400

    def validate_filter(self, filter):
        if filter not in [Filter.MOST_RECENT.name, Filter.LOWEST_PRICE.name, Filter.RELEVANCE.name]:
            return jsonify({'message': f"Filter {filter} not found"}), 400

    def validate_state(self, state):
        for state in state:
            if state not in all_states:
                return jsonify({'message': f"State {state} not found"}), 400

    def __init__(self, request: Request):
        input_json = request.get_json(force=False, silent=True)

        try:
            self.states = input_json['states']
            self.validate_state(self.states)
        except TypeError:
            self.states = all_states

        args = request.args
        self.search = args.get("search")

        self.page_start = args.get("page_start", None)
        if self.page_start is None:
            self.page_start = 0
        self.validate_page(self.page_start)

        self.page_end = args.get("page_end", None)
        if self.page_end is None:
            self.page_end = 0
        self.validate_page(self.page_end)

        self.price_min = args.get("price_min", None)
        if self.price_min is None:
            self.price_min = ''
        self.validate_price(self.price_min)
        self.price_max = args.get("price_max", None)
        if self.price_max is None:
            self.price_max = ''
        self.validate_price(self.price_max)

        self.filter = args.get("filter", None)
        if self.filter is None:
            self.filter = 'RELEVANCE'
        self.validate_filter(self.filter)
