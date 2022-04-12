from fastapi import APIRouter, Depends

from . import products, auth, users
from app.util.auth import oauth2_scheme


router = APIRouter()
router.include_router(auth.router)
router.include_router(users.router)
router.include_router(products.router, dependencies=[Depends(oauth2_scheme)])

