from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from lib.database.connection import Base, session

engine = create_engine('your_database_url')
Session = sessionmaker(bind=engine)
session = Session()

# Create the base class for the models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
