from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models, crud

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

print(crud.getPeople(db))
