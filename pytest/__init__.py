import pytest
from data import Product, products


# Product class
def test_product_class():
    product = Product(id=1, name='Soap', price=100)
    assert product.id == 1
    assert product.name == 'Soap'
    assert product.price == 200


