# lib/__init__.py
import sqlite3

CONN = sqlite3.connect('booking.db')
CURSOR = CONN.cursor()
