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


 
