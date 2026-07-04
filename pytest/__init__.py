import pytest
from data import Product, products


# Product class
def test_product_class():
    product = Product(id=1, name='Soap', price=100)
    assert product.id == 1
    assert product.name == 'Soap'
    assert product.price == 200

# To dict method
def test_to_dict() :
    product = Product(id=1, name='Soap', price=100)
    result = product.to_dict()
    assert result == {'id':1, 'name':'Soap', 'price':100}
    assert isinstance(result, dict)



