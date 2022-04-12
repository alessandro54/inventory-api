from fastapi import status, APIRouter, HTTPException, Form
from datetime import timedelta

from app.services.auth_service import authenticate_user, create_access_token

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()


@router.post("/token", status_code=status.HTTP_200_OK, tags=["auth"])
async def login(username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data=user, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}