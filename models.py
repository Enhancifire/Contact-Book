from database import Base
from sqlalchemy import Column, String, Text

class Person(Base):
    __tablename__ = "Person"

    id = Column(String, primary_key = True)
    Name = Column(String, primary_key = True)
    Address = Column(Text, primary_key = True)
    Email = Column(String, primary_key = True)
