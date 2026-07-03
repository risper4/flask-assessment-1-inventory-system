import requests
from flask import make_response, jsonify


# Product class
class Product() :
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def to_dict(self) :
        return {'id' : self.id, 'name' : self.name, 'price' : self.price}
    
# A list to store all the project instances
products = [
    Product(1, 'Peak milk', 200)
]


# Finds more product's details using a barcode from the api
def get_product_details(barcode) :
    url = f"https://world.openfoodfacts.net/api/v3.6/product/{barcode}.json"
    response = requests.get(url)
    data = response.json()
    return make_response(jsonify(data), 200)


