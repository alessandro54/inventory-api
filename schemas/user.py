from db.session import Base
from sqlalchemy import String, Integer, Boolean, Column, Text
from sqlalchemy.ext.declarative import DeclarativeMeta


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    email = Column(String(100), nullable=True, unique=True)
    name = Column(String(100), nullable=True)
    bio = Column(Text)
    disabled = Column(Boolean, default=False)