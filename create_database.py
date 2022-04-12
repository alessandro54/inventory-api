from app.db.session import Base, engine
from app.db.schemas import product, user

print("Creating db ....")

Base.metadata.create_all(engine)
