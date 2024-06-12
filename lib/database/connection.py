from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#def get_db_connection():
engine = create_engine('sqlite:///booking.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
    #return engine, Base, session

""" import sqlite3

DATABASE_NAME = './lib/database/booking.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn """