
import random
from models.sensor_data import SensorData
from models.db import Session
from sqlalchemy import func

class SensorDataService:

    def add_sensors(sensorNumber):

        session = Session()
    
        for i in range(1,sensorNumber+1):
            sensor_data = SensorData()
            sensor_data.temperature = random.randint(8,15)
            sensor_data.wind_speed = random.randint(15,25)
            sensor_data.relative_humidity = random.randint(40,70)
            sensor_data.co2 = random.randint(500,1500)
            sensor_data.sensor_id = i
            session.add(sensor_data) 
       
        session.commit()

    def get_sensor_stats():
        session = Session()
        result = (
            session.query(
                SensorData.sensor_id,
                func.max(SensorData.co2).label('max_co2'),
                func.avg(SensorData.co2).label('avg_co2'),
                func.min(SensorData.co2).label('min_co2'),
                func.max(SensorData.temperature).label('max_temperature'),
                func.avg(SensorData.temperature).label('avg_temperature'),
                func.min(SensorData.temperature).label('min_temperature'),
                func.max(SensorData.wind_speed).label('max_wind_speed'),
                func.avg(SensorData.wind_speed).label('avg_wind_speed'),
                func.min(SensorData.wind_speed).label('min_wind_speed'),
                func.max(SensorData.relative_humidity).label('max_relative_humidity'),
                func.avg(SensorData.relative_humidity).label('avg_relative_humidity'),
                func.min(SensorData.relative_humidity).label('min_relative_humidity')
            )
            .group_by(SensorData.sensor_id)
            .order_by(SensorData.sensor_id)  # Order the results by sensor_id
            .all()
        )

        return result


