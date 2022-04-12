from app.db.session import Base, engine

print("Creating db ....")

Base.metadata.create_all(engine)
