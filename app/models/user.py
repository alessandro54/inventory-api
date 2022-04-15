from app.db.session import Base
from sqlalchemy import String, Integer, Boolean, Column, Text


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    email = Column(String(100), nullable=True, unique=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    bio = Column(Text)
    disabled = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User username={self.username} fullname={self.first_name} {self.last_name} email={self.email}>"