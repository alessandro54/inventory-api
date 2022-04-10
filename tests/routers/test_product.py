from tests import client


def test_get_products():
    response = client.get("/v1/api/products")
    assert response.status_code == 200
    assert response.json() == {"products": []}
