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
    product = next((p for p in products if p.id == id), None)
    if product :
        return jsonify(product.to_dict()), 200
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


@app.route('/inventory/<int:id>',methods=['PATCH'])
def update_product(id) :
    data = request.get_json()
    product = next((p for p in products if p.id == id), None)
    if not product:
        return jsonify('Product not found'), 404
    else :
        if 'name' in data :
            product.name = data['name']
    return jsonify(product.to_dict())

if __name__ == '__main__' :
    app.run(port=5555, debug=True)