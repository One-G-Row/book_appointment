# main.py
from lib.database.connection import session
from lib.models.doctor import Doctor
from lib.models.user import User
from lib.models.appointment import Appointment

def main():
    # Get user input
    user_name = input("Enter user's name: ")
    user_email = input("Enter user's email: ")
    doctor_name = input("Enter doctor's name: ")
    appointment_date = input("Enter appointment date: ")
    appointment_time = input("Enter appointment time: ")

    # Create a doctor
    new_doctor = Doctor(name=doctor_name)
    session.add(new_doctor)
    session.commit()
    doctor_id = new_doctor.id  # fetch the id of the newly created doctor

    # Create a user
    new_user = User(name=user_name, email=user_email)
    session.add(new_user)
    session.commit()
    user_id = new_user.id  # fetch the id of the newly created user

    # Create an appointment
    new_appointment = Appointment(date=appointment_date, time=appointment_time, doctor_id=doctor_id, user_id=user_id)
    session.add(new_appointment)
    session.commit()
    appointment_id = new_appointment.id  # fetch the id of the newly created appointment

    # Query the database for inserted records
    doctors = session.query(Doctor).all()
    users = session.query(User).all()
    appointments = session.query(Appointment).all()

    # Close the session
    session.close()

    # Display results
    print("\nDoctors:")
    for doctor in doctors:
        print(f'Doctor {doctor.id}, Name: {doctor.name}')

    print("\nUsers:")
    for user in users:
       print(f'User {user.id}, Name: {user.name}, Email: {user.email}')

    print("\nAppointments:")
    for appointment in appointments:
         print(f'Appointment {appointment.id}, Date: {appointment.date}, Time: {appointment.time},'
              f'Doctor ID: {appointment.doctor_id}, User ID: {appointment.user_id}')

if __name__ == "__main__":
    main()



""" from lib.database.setup import create_tables
from lib.database.connection import get_db_connection
#from __init__ import CURSOR, CONN

def main():
    create_tables()
    conn = get_db_connection()
    cursor = conn.cursor()

    #get user input 
    user_name = input("Enter user's name: ")
    user_email = input("Enter user's email: ")
    doctor_name = input("Enter doctor's name: ")
    appointment_date = input("Enter appointment date: ")
    appointment_time = input("Enter appointment time: ")


  # Create a doctor
    cursor.execute('INSERT INTO doctors (name) VALUES (?)', (doctor_name,))
    doctor_id = cursor.lastrowid  # fetch the id of the newly created doctor

    # Create a user
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (user_name, user_email))
    user_id = cursor.lastrowid  # fetch the id of the newly created user

    # Create an appointment
    cursor.execute('INSERT INTO appointments (date, time, doctor_id, user_id) VALUES (?, ?, ?, ?)', 
                   (appointment_date, appointment_time, doctor_id, user_id))
    appointment_id = cursor.lastrowid  # fetch the id of the newly created appointment

    conn.commit()

     # Query the database for inserted records.

    cursor.execute('SELECT * FROM doctors')
    doctors = cursor.fetchall()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    cursor.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()

    conn.close()

    # Display results
    print("\nDoctors:")
    for doctor in doctors:
        print(f'Doctor {doctor["id"]}, Name: {doctor["name"]}')

    print("\nUsers:")
    for user in users:
       print(f'User {user["id"]}, Name: {user["name"]}, Email: {user["email"]}')

    print("\nAppointments:")
    for appointment in appointments:
         print(f'Appointment {appointment["id"]}, Date: {appointment["date"]}, Time: {appointment["time"]},'
              f'Doctor ID: {appointment["doctor_id"]}, User ID: {appointment["user_id"]}')
               
             
"""  """
if __name__ == "__main__":
    main() """