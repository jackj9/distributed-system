import os
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models.sensor_data import Base,SensorData

load_dotenv()



DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOSTNAME = os.environ.get("DB_HOSTNAME")
DB_NAME = os.environ.get("DB_NAME")

connection_string = f'Driver=ODBC Driver 17 for SQL Server;Server={DB_HOSTNAME};Database={DB_NAME};Uid={DB_USERNAME};Pwd={DB_PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

# Create the SQLAlchemy engine
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine, checkfirst=True)