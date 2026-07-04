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


# GET all products
def test_get_all_products(client) :
    response = client.get('/inventory')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['name'] == 'Apples'