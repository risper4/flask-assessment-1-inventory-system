import pytest

from app import app
from data import products, Product

@pytest.fixture
def client() :
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_products():
    products.clear()
    products.append(Product(id=1, name='Apples', price=50))
    yield
    
