import datetime
import logging
import azure.functions as func
from services.sensor_data_service import SensorDataService
from models.sensor_data import SensorData
from models.db import Session

def main(myTimer: func.TimerRequest) -> None:

    # utc_timestamp = datetime.datetime.utcnow().replace(
    #     tzinfo=datetime.timezone.utc).isoformat()

    # if myTimer.past_due:
    #     logging.info('The timer is past due!')

    # logging.info('Python timer trigger function ran at %s', utc_timestamp)

    # Your logic for adding sensors
    SensorDataService.add_sensors(20)
