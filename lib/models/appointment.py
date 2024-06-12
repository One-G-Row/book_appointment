from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
#from database.connection import Base, session
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
#from lib.database.connection import Base, session

engine = create_engine('your_database_url')
Session = sessionmaker(bind=engine)
session = Session()

# Create the base class for the models
Base = declarative_base()

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key = True, autoincrement = True)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    doctor = relationship("Doctor")
    user = relationship("User")