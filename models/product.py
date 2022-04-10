from database import Base
from sqlalchemy import String,Integer, Column, Text


class ProductSchema(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Product name={self.name} price={self.price}>"
