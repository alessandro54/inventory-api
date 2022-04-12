from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from app.db.session import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
api_router = APIRouter(prefix="/v1/api")
root_router = APIRouter()
db = SessionLocal()
