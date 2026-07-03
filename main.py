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


def add_product(args) :
    new_id = max((p.id for p in products)) + 1 if products else 1
    new_product = Product(id=new_id, name=args.name)
    products.append(new_product)
    print(f'✅ Product {args.name} added successfully added')


def update_product(args) :
    id = args.id
    product = next((p for p in products if p.id == id), None)
    if not product :
        print('❌ Product not found')
        return
    else :
        product.name = args.name
        print(f'✅ Product {args.id} successfully updated')
        print(product.to_dict())


def delete_product(args) :
    id = args.id
    global products
    product = next((p for p in products if p.id == id), None)
    if not product :
        print('❌ Product not found')
        return
    else :
        products = [p for p in products if p.id != id]
        return('✅ Product successfully added')

    
