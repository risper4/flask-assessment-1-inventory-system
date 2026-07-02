from flask import Flask, request, jsonify
from data import Product, products, get_product_details

app = Flask(__name__)


# GET : Retrieves all products
@app.route('/inventory', methods=['GET'])
def show_products() :
    return jsonify(p.to_dict() for p in products)


# GET : Retrieves a specific product
@app.route('/inventory/<int:id>', methods=['GET'])
def show_product(id) :
    event = next((p for p in products if p.id == id), None)
    return jsonify(event.to_dict())

if __name__ == '__main__' :
    app.run(port=5555, debug=True)