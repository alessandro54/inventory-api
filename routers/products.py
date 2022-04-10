from . import router


@router.get("/products/", tags=["products"])
async def get_products():
    return [
        {"aaa": "aaa"}
    ]


@router.get('/products/{id}', tags=["products"])
async def get_product(identifier: str):
    return [
        {"aaa": identifier}
    ]
