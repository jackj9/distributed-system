import datetime
import logging
import azure.functions as func
from services.sensor_data_service import SensorDataService
from models.sensor_data import SensorData
from models.db import Session


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    SensorDataService.add_sensors(20)
    return func.HttpResponse(
            status_code=200
        )