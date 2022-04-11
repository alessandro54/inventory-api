from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from db.session import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter(prefix="/v1/api")
db = SessionLocal()
