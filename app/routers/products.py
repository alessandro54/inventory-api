from fastapi import APIRouter, HTTPException
from typing import List

from app.db import db
from app.schemas.product import Product as ProductSchema
from app.models.product import Product


router = APIRouter(prefix="/v1/api")


@router.get("/products", response_model=List[ProductSchema], status_code=200, tags=["products"])
async def get_all_products():
    items = db.query(Product).all()
    return items


@router.get("/products/{product_id}", response_model=ProductSchema, status_code=200, tags=["products"])
async def get_product(product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Resource not found")


@router.post("/products", response_model=ProductSchema, status_code=201, tags=["products"])
async def create_product(product: ProductSchema):
    return product


@router.put("/products/{product_id}", response_model=ProductSchema, status_code=200, tags=["products"])
async def update_product(product_id: str):
    return product_id


@router.delete("/products/{product_id}", response_model=ProductSchema, status_code=200, tags=["products"])
async def delete_product(product_id: str):
    return product_id
