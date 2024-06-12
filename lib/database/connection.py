# lib/database/connection.py
# If using raw SQLite connections, but not needed with SQLAlchemy ORM
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('booking.db')
    return conn


""" import sqlite3

DATABASE_NAME = './lib/database/booking.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn """