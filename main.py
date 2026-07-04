import argparse

import requests

url = 'http://127.0.0.1:5555'

def show_products(args) :
    response = requests.get(f'{url}/inventory')
    response.raise_for_status()
    print('These are the products : ')
    for product in response.json() :
        print(product)


def show_product_by_id(args) :
    id = args.id
    response = requests.get(f'{url}/inventory/{id}')
    response.raise_for_status()
    data = response.json()
    print(data)
    


def create_product(args) :
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
    display_product_by_id.add_argument('--id', required=True, type=int)
    display_product_by_id.set_defaults(func=show_product_by_id)


    #Add a new product
    add_product = subparser.add_parser('add-product', help='Adds a new product to inventory')
    add_product.add_argument('--name', required=True)
    add_product.add_argument('--price', required=True, type=int)
    add_product.set_defaults(func=create_product)


    #Update a specific product
    update_item = subparser.add_parser('update-product', help='Updating a specific product')
    update_item.add_argument('--id', required=True, type=int)
    update_item.add_argument('--price', required=True, type=int)
    update_item.set_defaults(func=update_product)


    #Delete a specific product
    remove_product = subparser.add_parser('delete-product', help='Deletes a specific product')
    remove_product.add_argument('--id', required=True, type=int)
    remove_product.set_defaults(func=delete_product)


    #Find details in the api
    find_details = subparser.add_parser('find-details', help='Finds a product details in the api')
    find_details.add_argument('--barcode')
    find_details.set_defaults(func=get_product_details)


    args = parser.parse_args() 

    if hasattr(args, 'func') :
        args.func(args)
    else :
        parser.print_help()



if __name__ == '__main__' :
    main()
