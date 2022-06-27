#  This file is for storing settiings for db creation`

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#First sertup a URL for accessing dabatabse
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost/iprojectdb'

#Second Setup the engine for running sqlalchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#For talking with database we have to set an session 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #https://fastapi.tiangolo.com/tutorial/sql-databases/

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
