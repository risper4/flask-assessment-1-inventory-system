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
    if event :
        return jsonify(event.to_dict()), 200
    else : 
        return jsonify("Product not found"), 404


# POST : Creates new product
@app.route('/inventory', methods=['POST'])
def create_product() :
    data = request.get_json()
    new_id = max((p.id for p in products)) + 1 if products else 1
    new_product = Product(id=new_id, name=data['name'])
    products.append(new_product)
    return jsonify(new_product.to_dict()), 200

if __name__ == '__main__' :
    app.run(port=5555, debug=True)