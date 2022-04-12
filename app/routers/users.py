from fastapi import Depends, HTTPException, status

from . import root_router as router, db, oauth2_scheme
from app.models.user import User as UserModel
from app.services.users_service import get_current_active_user


@router.get("/user/profile", response_model=UserModel, tags=["user"])
async def get_profile(current_user: UserModel = Depends(get_current_active_user)):
    return current_user

@router.post("/user/create",tags=["user"])
async def create_user():
    return None
