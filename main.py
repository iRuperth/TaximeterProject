import time
import logging
import os
from journey_database import init_db, log_journey
from taxi import Taxi
from authentication import driver_auth

if __name__ == "__main__":
    init_db()
    authenticated_user_id = driver_auth()
    taxi_app = Taxi(authenticated_user_id)
    taxi_app.welcome_passenger()
    if taxi_app.continue_journey:
        taxi_app.start_journey_loop()
        taxi_app.end_journey()
