from fastapi import status, HTTPException
from . import router, db
from models.product import Product as ProductModel
from schemas.product import Product
from typing import List


@router.get("/products/",
            response_model=List[ProductModel],
            status_code=status.HTTP_200_OK,
            tags=["products"])
async def get_products():
    items = db.query(Product).all()
    return items


@router.get("/products/{id}",
            response_model=ProductModel,
            status_code=status.HTTP_200_OK,
            tags=["products"])
async def get_product(product_id: str):
    item = db.query(Product).filter(Product.id == product_id).first()
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Resource not found")
