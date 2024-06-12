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
for doc in doctors:
    new_doc = Doctor(id=doc[0], name=doc[1])
    session.add(new_doc)
session.commit()

# Fetch and insert users
old_cursor.execute('SELECT id, name, email FROM users')
users = old_cursor.fetchall()
for usr in users:
    new_user = User(id=usr[0], name=usr[1], email=usr[2])
    session.add(new_user)
session.commit()

# Fetch and insert appointments
old_cursor.execute('SELECT id, date, time, doctor_id, user_id FROM appointments')
appointments = old_cursor.fetchall()
for app in appointments:
    new_app = Appointment(id=app[0], date=app[1], time=app[2], doctor_id=app[3], user_id=app[4])
    session.add(new_app)
session.commit()

# Close the old database connection
old_conn.close()

# Close the SQLAlchemy session
session.close()
