from db.session import Base, engine
from schemas.product import Product
from schemas.user import User


print("Creating db ....")

Base.metadata.create_all(engine)
