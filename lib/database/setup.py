# lib/database/setup.py

from lib.database import create_tables

def main():
    create_tables()

if __name__ == "__main__":
    main()

""" from .connection import get_db_connection

def create_tables():
   conn = get_db_connection()
   cursor = conn.cursor()

   cursor.execute('''
      CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        )
     ''')
   
   cursor.execute(''' 
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
        )
     ''')

   cursor.execute('''
     CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        doctor_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY (doctor_id) REFERENCES doctors (id),
        FOREIGN KEY (user_id) REFERENCES users (id)
        )
     ''')

   conn.commit()
   conn.close()


 """