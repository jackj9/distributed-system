import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class SensorData(Base):
    __tablename__ = 'sensor_data'    
    id = Column(String(36), primary_key=True, nullable=True, unique=True)
    temperature = Column(Integer)
    wind_speed = Column(Integer)
    relative_humidity = Column(Integer)
    co2 = Column(Integer)
    sensor_id = Column(Integer)

    def __init__(self):
        self.id = str(uuid.uuid4())

