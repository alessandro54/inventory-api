from datetime import datetime, timedelta

from jose import jwt
from pydantic import BaseModel

from app.db import db
from app.models.user import User
from app.util.auth import SECRET_KEY, ALGORITHM, pwd_context


class Token(BaseModel):
    access_token: str
    token_type: str


def authenticate_user(username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: User | bool, expires_delta: timedelta | None = None):
    print(data)
    to_encode = {
        "username": data.username,
        "password": data.password
    }
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
