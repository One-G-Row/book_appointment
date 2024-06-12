
from sqlalchemy import Column, Integer, String
from lib.database.connection import Base, session
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
#from lib.database.connection import Base, session

engine = create_engine('your_database_url')
Session = sessionmaker(bind=engine)
session = Session()

# Create the base class for the models
Base = declarative_base()

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable = False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int) and len(id) > 0:
            self._id = id
        else:
            raise ValueError("Enter available docor id")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Enter available doctor name")

    @classmethod
    def get_all(cls):
        return session.query(cls).all()
        
    @classmethod
    def find_by_id(cls, id):
      return session.query(cls).filter_by(id=id).first()
    
    @classmethod
    def find_by_name(cls, name):
      return session.query(cls).filter_by(name=name).first()
        
    def save(self):
        session.add(self)
        session.commit()

        