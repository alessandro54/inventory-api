import uuid

from sqlalchemy import String, Integer, Column, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from app.db.session import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    upc = Column(String(12), unique=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    unit_price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    def __repr__(self):
        return f"<Product name={self.name} unit_price={self.unit_price}>"
