from fastapi import status, APIRouter, HTTPException

from app.db import db
from app.models.product import Product as ProductModel
from app.db.schemas.product import Product
from typing import List

router = APIRouter(prefix="/v1/api")


@router.get("/products", response_model=List[ProductModel], status_code=status.HTTP_200_OK, tags=["products"])
async def get_all_products():
    items = db.query(Product).all()
    return items


@router.get("/products/{product_id}",
            response_model=ProductModel,
            status_code=status.HTTP_200_OK,
            tags=["products"])
async def get_product(product_id: str):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Resource not found")


@router.post("/products",
             response_model=ProductModel,
             status_code=status.HTTP_201_CREATED,
             tags=["products"])
async def create_product(product: ProductModel):
    return product


@router.put("/products/{id}",
            response_model=ProductModel,
            status_code=status.HTTP_200_OK,
            tags=["products"])
async def update_product(product_id: int):
    return product_id


@router.delete("/products/{id}",
               response_model=ProductModel,
               status_code=status.HTTP_200_OK,
               tags=["products"])
async def delete_product(product_id: int):
    return product_id
