from fastapi import FastAPI
from database import SessionLocal
from routers import products

app = FastAPI()
# Routers
app.include_router(products.router)
db = SessionLocal()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
