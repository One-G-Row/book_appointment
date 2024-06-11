# lib/helpers.py
from models.doctor import Doctor
from models.user import User
from models.appointment import Appointment

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_doctors():
    doctors = Doctor.get_all()
    for doctor in doctors:
        print(doctors)

def find_doctor_by_name():
    name = input("Enter the doctor's name: ")
    doctor = Doctor.find_by_name(name)
    print(doctor) if doctor else print(
       f'Doctor {name} not found' )
    
def find_doctor_by_id():
    name = input("Enter the doctor's id: ")
    doctor = Doctor.find_by_id(id)
    print(doctor) if doctor else print(
       f'Doctor {id} not found' )
    