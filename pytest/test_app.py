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


# GET product by id
def test_specific_product(client) :
    response = client.get('/inventory/1')
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Apples'

def test_product_not_found(client) : 
    response = client.get('/inventory/500')
    assert response.status_code == 404

# POST a new product
def test_create_product(client) :
    response = client.post('/inventory', json={'name':'Prime flour', 'price':169})
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data['name'] == 'Milk'
    assert data['id'] == 2