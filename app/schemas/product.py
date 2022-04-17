from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    upc: str
    description: str | None = None
    unit_price: float
    quantity: int


class Product(ProductBase):
    id: str

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass
