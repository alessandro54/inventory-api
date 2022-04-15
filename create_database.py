from app.db.session import Base, engine
from app.models import user, product

print("Creating db ....")

Base.metadata.create_all(engine)
