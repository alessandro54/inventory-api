from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException, Form

from app.db.schemas.user import User
from app.models.user import User as UserModel, UserForm
from app.services.users_service import get_current_active_user
from app.services.auth_service import get_password_hash, create_access_token
from app.db import db

router = APIRouter()


@router.get("/user/profile", response_model=UserModel, tags=["user"])
async def get_profile(current_user: UserModel = Depends(get_current_active_user)):
    return current_user


def check_username_uniqueness(username: str):
    user = db.query(User).filter(User.username == username).first()
    if user is not None:
        raise HTTPException(status_code=400, detail="Username already taken")


def check_password_match(password, password_confirmation):
    if password != password_confirmation:
        raise HTTPException(status_code=400, detail="Passwords does not match")


@router.post("/user/create", tags=["user"])
async def create_user(payload: UserForm = Depends()):
    check_username_uniqueness(payload.username)
    check_password_match(payload.password, payload.password_confirmation)
    new_user = User(
        username=payload.username,
        password=get_password_hash(payload.password)
    )
    db.add(new_user)
    db.commit()
    access_token = create_access_token(
        data=new_user, expires_delta=timedelta(30)
    )
    return {"access_token": access_token, "token_type": "bearer"}
