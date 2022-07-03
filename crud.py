import models
import database
from sqlalchemy.orm import Session

def getPeople(db: Session):
    db.query(models.Person).all()
