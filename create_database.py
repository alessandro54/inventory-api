from db.session import Base, engine
from schemas.product import Product


print("Creating db ....")

Base.metadata.create_all(engine)
