from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace 'sqlite:///example.db' with your database connection string
engine = create_engine('sqlite:///example.db', echo=True)

Session = sessionmaker(bind=engine)
