from fastapi import Depends, APIRouter

from app.models.user import User as UserModel
from app.services.users_service import get_current_active_user


router = APIRouter()


@router.get("/user/profile", response_model=UserModel, tags=["user"])
async def get_profile(current_user: UserModel = Depends(get_current_active_user)):
    return current_user


@router.post("/user/create", tags=["user"])
async def create_user():
    return None
