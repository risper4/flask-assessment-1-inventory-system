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
    new_product = Product(id=new_id, name=args.name, price=args.price)
    products.append(new_product)
    print(f'✅ Product {args.name} added successfully added')


def update_product(args) :
    id = args.id
    product = next((p for p in products if p.id == id), None)
    if not product :
        print('❌ Product not found')
        return
    else :
        product.price = args.price
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
    

def get_product_details(args) :
    barcode = args.barcode
    get_product_details(barcode)


def main() :
    parser = argparse.ArgumentParser(description='Inventory Mnagement')
    subparser = parser.add_subparsers()


    #Displaying all products
    display_all_products = subparser.add_parser('inventory', help='Displays all products')
    display_all_products.set_defaults(func=show_products)

    #Display a product by id
    display_product_by_id = subparser.add_parser('display-product', help='Dispays a product by its id')
    display_product_by_id.add_argument('--id')
    display_product_by_id.set_defaults(func=show_product_by_id)


    #Add a new product

    
