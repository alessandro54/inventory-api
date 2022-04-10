from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    price: str

    class Config:
        orm_mode = True
