from fastapi import status, HTTPException, Depends
from . import router, db, oauth2_scheme
from models.product import Product as ProductModel
from schemas.product import Product
from typing import List


@router.get("/products", response_model=List[ProductModel], status_code=status.HTTP_200_OK, tags=["products"])
async def get_all(token: str = Depends(oauth2_scheme)):
    items = db.query(Product).all()
    return items


@router.get("/products/{product_id}",
            response_model=ProductModel,
            status_code=status.HTTP_200_OK,
            tags=["products"])
async def get(product_id: str, token: str = Depends(oauth2_scheme)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Resource not found")


@router.post("/products",
             response_model=ProductModel,
             status_code=status.HTTP_201_CREATED,
             tags=["products"])
async def create(product: ProductModel, token: str = Depends(oauth2_scheme)):
    return product


@router.put("/products/{id}",
            response_model=ProductModel,
            status_code=status.HTTP_200_OK,
            tags=["products"])
async def update(product_id: int, token: str = Depends(oauth2_scheme)):
    return product_id


@router.delete("/products/{id}",
               response_model=ProductModel,
               status_code=status.HTTP_200_OK,
               tags=["products"])
async def delete(product_id: int, token: str = Depends(oauth2_scheme)):
    return product_id
