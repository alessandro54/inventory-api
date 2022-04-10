from . import router, db
from models.product import Product as Model
from schemas.product import Product
from typing import List


@router.get("/products/", response_model=List[Model], status_code=200, tags=["products"])
async def get_products():
    items = db.query(Product).all()
    return items


@router.get('/products/{id}', tags=["products"])
async def get_product(identifier: str):
    return [
        {"aaa": identifier}
    ]
