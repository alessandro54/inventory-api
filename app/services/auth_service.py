from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt

from app.routers import db
from app.db.schemas.user import User


SECRET_KEY = "e8645c4bcb2b6bb9019bdc4b5c29b105a3c99369c0de5cf456c993421c451bc1"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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