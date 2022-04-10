from fastapi import APIRouter
from db.session import SessionLocal

router = APIRouter(prefix="/v1/api")
db = SessionLocal()
