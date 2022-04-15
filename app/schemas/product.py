from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: str

    class Config:
        orm_mode = True
