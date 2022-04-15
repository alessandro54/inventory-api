from sqlalchemy import String, Integer, Column, Text, DateTime
from datetime import datetime

from app.db.session import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    def __repr__(self):
        return f"<Product name={self.name} price={self.price}>"
