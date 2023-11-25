import json
import logging
from models.db import Session
import azure.functions as func
from services.sensor_data_service import SensorDataService

import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    sensor_data = SensorDataService.get_sensor_stats()
    response_data = {}
    for stat in sensor_data:
        response_data[f"{stat.sensor_id}_co2"] = f"Max CO2: {stat.max_co2}, Avg CO2: {stat.avg_co2}, Min CO2: {stat.min_co2},"
        response_data[f"{stat.sensor_id}_temp"] = f"Max CO2: {stat.max_temperature}, Avg CO2: {stat.avg_temperature}, Min CO2: {stat.min_temperature},"
        response_data[f"{stat.sensor_id}_wind"] = f"Max CO2: {stat.max}, Avg CO2: {stat.avg}, Min CO2: {stat.min},"
        response_data[f"{stat.sensor_id}_humidity"] = f"Max CO2: {stat.max_relative_humidity}, Avg CO2: {stat.avg_relative_humidity}, Min CO2: {stat.min_relative_humidity},"
  
    return func.HttpResponse(
            json.dumps(response_data),
            mimetype="application/json",
            status_code=200
        )