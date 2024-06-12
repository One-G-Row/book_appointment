# migrate_data.py
import sqlite3
from database import session
from models import Doctor, User, Appointment

# Connect to the old database
old_conn = sqlite3.connect('old_booking.db')
old_cursor = old_conn.cursor()

# Fetch and insert doctors
old_cursor.execute('SELECT id, name FROM doctors')
doctors = old_cursor.fetchall()
for doctor in doctors:
    new_doctor = Doctor(id=doctor[0], name=doctor[1])
    session.add(new_doctor)
session.commit()

# Fetch and insert users
old_cursor.execute('SELECT id, name, email FROM users')
users = old_cursor.fetchall()
for user in users:
    new_user = User(id=user[0], name=user[1], email=user[2])
    session.add(new_user)
session.commit()

# Fetch and insert appointments
old_cursor.execute('SELECT id, date, time, doctor_id, user_id FROM appointments')
appointments = old_cursor.fetchall()
for appointment in appointments:
    new_appointment = Appointment(id=appointment[0], date=appointment[1], time=appointment[2], doctor_id=appointment[3], user_id=appointment[4])
    session.add(new_appointment)
session.commit()

# Close the old database connection
old_conn.close()

# Close the SQLAlchemy session
session.close()
