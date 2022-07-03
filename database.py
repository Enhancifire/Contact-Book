from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = "sqlite:///contacts.db"

engine = create_engine(
        SQLALCHEMY_DATABASE_URI,
        )

SessionLocal = sessionmaker(autocommit = False, autoflush = False)

Base = declarative_base()