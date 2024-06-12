from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key = True, autoincrement = True)
    date = Column(String)
    time = Column(String)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    doctor = relationship("Doctor")
    user = relationship("User")