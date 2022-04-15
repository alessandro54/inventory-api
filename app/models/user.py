from datetime import datetime
from sqlalchemy import String, Integer, Boolean, Column, Text, DateTime

from app.db.session import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    email = Column(String(100), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    bio = Column(Text)
    disabled = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    def __repr__(self):
        return f"<User username={self.username} fullname={self.first_name} {self.last_name} email={self.email}>"