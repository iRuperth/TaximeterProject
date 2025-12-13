import time
import logging
import os
from taxi import Taxi
from log_journey import log_journey

if __name__ == "__main__":
    # OOP Execution Flow:
    taxi_app = Taxi()
    taxi_app.welcome_passenger()
    taxi_app.logger = log_journey
    if taxi_app.continue_journey:
        taxi_app.start_journey_loop()
        taxi_app.end_journey()


# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')
