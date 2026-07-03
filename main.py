import argparse

from data import products, Product, get_product_details

def show_products(args) :
    if not products :
        print('❌No current products yet')
        return
    else :
        for p in products :
            print('These are the current products : ')
            print(p.to_dict())


def show_product_by_id(args) :
    id = args.id
    product = next((p for p in products if p.id == id), None)
    if product :
        print(product.to_dict())
    else :
        print('❌ Product not found')


