from flask import Flask, request, jsonify
from data import Product, products, get_product_details

app = Flask(__name__)


@app.route('/inventory', methods=['GET'])
def show_products() :
    return jsonify(p.to_dict() for p in products)


if __name__ == '__main__' :
    app.run(port=5555, debug=True)