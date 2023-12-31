import json
import logging
from models.db import Session
import azure.functions as func
from services.sensor_data_service import SensorDataService


def main(changes):
    
    logging.info("Trigger executed successfully.")
    senor_data = SensorDataService.get_sensor_stats()
    
    for stat in senor_data:
        logging.info(f"Sensor ID: {stat.sensor_id}, Max CO2: {stat.max_co2}, Avg CO2: {stat.avg_co2}, Min CO2: {stat.min_co2}, ")
        logging.info(f"Sensor ID: {stat.sensor_id}, Max Temperature: {stat.max_temperature}, Avg Temperature: {stat.avg_temperature}, Min Temperature: {stat.min_temperature}, ")
        logging.info(f"Sensor ID: {stat.sensor_id}, Max Wind Speed {stat.max_wind_speed}, Avg Wind Speed {stat.avg_wind_speed}, Min Wind Speed {stat.min_wind_speed}, ")
        logging.info(f"Sensor ID: {stat.sensor_id}, Max Relative Humidity {stat.max_relative_humidity}, Avg Relative Humidity {stat.avg_relative_humidity}, Min Relative Humidity {stat.min_relative_humidity}, ")
    




