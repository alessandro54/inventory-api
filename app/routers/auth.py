from datetime import timedelta
from app.services import auth_service
from fastapi import status, HTTPException, Form
from . import root_router as router

ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post("/token", status_code=status.HTTP_200_OK, tags=["auth"])
async def login(username: str = Form(...), password: str = Form(...)):
    user = auth_service.authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(
        data=user, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}