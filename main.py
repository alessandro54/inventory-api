from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException, status, Form
from routers import products
from routers import users
from routers.users import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, authenticate_user, Token

app = FastAPI()


# Routers
app.include_router(products.router)
app.include_router(users.router)


@app.post("/token", status_code=status.HTTP_200_OK, tags=["token"])
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


