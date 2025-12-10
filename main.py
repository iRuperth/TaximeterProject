import time
import logging
import os

#Main variables.
stopped_rate_day = 0.02
moving_rate_day = 0.05
base_rate_day = 10.0
stopped_rate_nocturne = 0.20
moving_rate_nocturne = 0.40
base_rate_nocturne = 20.0

#Clear console function.
    # def clear_console():
    #     os.system('cls' if os.name == 'nt' else 'clear')

#Logging function.
def log_journey( name, total_duration, total_price):
    fareContent = f"Name: {name}\n"
    fareContent += f"Total duration: {total_duration:.2f} seconds\n"
    fareContent += f"Total price: {total_price:.2f} €\n" 
    fareContent += "\n" 
    try:
        #Using "with open" to append the fare content to the historical.txt file.
        with open("historical.txt", "a", encoding='utf-8') as file:
                file.write(fareContent)
    except IOError:
            print("Error trying to write to historical.txt")

class Taxi:
    def __init__(self):
        # Rates will be set by set_rates_from_time
        self.base_rate = 0.0
        self.stopped_rate = 0.0
        self.moving_rate = 0.0

        # Journey state attributes
        self.passenger_name = None
        self.total_price = 0.0
        self.total_duration = 0.0
        self.current_state = "moving" 
        self.start_time_journey = None
        self.start_time_state = None
        self.continue_journey = False
        #Composition.
        self.logger = log_journey
    
    def set_rates_from_time(self):
        while True:
            time_input_str = input("Insert the current time: 0-23h format: ").strip()
            logging.warning(f'User input time: {time_input_str}') # New log
            try:
                time_input = int(time_input_str)
                if 0 <= time_input <= 23:
                    if time_input >= 18 or time_input <= 6:
                        print("The nigh's young, Starting the car...")
                        self.stopped_rate = stopped_rate_nocturne
                        self.moving_rate = moving_rate_nocturne
                        self.base_rate = base_rate_nocturne
                        return
                    else:
                        print("Wonderful day today, Starting the car...")
                        self.stopped_rate = stopped_rate_day
                        self.moving_rate = moving_rate_day
                        self.base_rate = base_rate_day
                        return
                else:
                    print("Incorrect time, try again.")
            except ValueError:
                print("Come on, just see your watch.")

    def welcome_passenger(self):
        # clear_console()
        self.set_rates_from_time() # Calling the internal method to set rates.

        logging.warning('Starting working') 
        print(" Welcome to our digital Taxi")
        print("\n")
        print(" Welcome again! Please enter the passenger name:")
        name = input().strip()
        logging.warning(f'First user input name: {name}')
        self.passenger_name = name
        print("\n")
        print(f" Helloo, {self.passenger_name}!")
        print(f" The minimun fare is {self.base_rate:.2f} €.")
        print(f" The stop fare is {self.stopped_rate:.2f}€ per second.")
        print(f" The moving fare is {self.moving_rate:.2f}€ per second.")
        print("\n")
        print(" Do you wish to continue? (y/n)")
        answer = input().strip().lower()
        logging.warning(f'Second user input continue answer: {answer}') # New log
        if answer == "y":
            print(" Great, let's go!")
            self.total_price = self.base_rate
            self.continue_journey = True
        else:
            print(" We hope to see you again!")
            self.continue_journey = False
    
    def set_time_journey(self):
        self.start_time_journey = time.time()
        self.start_time_state = self.start_time_journey
        # current_state = "Moving" Starting state.
        print("\n Be welcome and enjoy your journey! Current state: moving")
        print(f" Current fare: {self.total_price:.2f} €.")
        print(" Instructions: Use 'S' for stop, 'M' for move, and 'X' for exit.")
        logging.warning('Instructions working') 


        #private method.
    def _update_fare_duration(self, current_time):
        duration = current_time - self.start_time_state
        if self.current_state == "moving":
            self.total_price += self.moving_rate * duration
        else:
            self.total_price += self.stopped_rate * duration
        self.start_time_state = current_time
        return duration

    def start_journey_loop(self):
        self.set_time_journey()
        #Starting infinite loop for the journey.
        while True:
            #waiting for the user to input "  ".
            answer = input(" ").strip().lower()
            logging.warning(f'User input command: {answer}') # New log
            current_time = time.time()
            self._update_fare_duration(current_time)

            if answer == "s":
                print(" Traffic lights, good heavens!!")
                self.current_state = "stopped"
                logging.warning('Stopped working') 

            elif answer == "m":
                print(" here we go!")
                self.current_state = "moving"
                logging.warning('Moving working') 

            elif answer == "x":
                print(" Lets park...")
                logging.warning('Parking working') 
                time.sleep(3)
                print(" Generating the receipt...")
                time.sleep(2)
                logging.warning('Printer working') 
                print(" Printer sound.")
                time.sleep(2)
                break
                
            else:
                print(" Ouch, Technical error! \n Try to press the right key. (S to stop, M to move, X to exit)")

    def end_journey(self):
        end_time_journey = time.time()
        self.total_duration = end_time_journey - self.start_time_journey
        
        print("\n----------------------------------------")
        print("            JOURNEY SUMMARY           ")
        print("--------------------------------------")
        print(f" Total duration: {self.total_duration:.2f} Seconds.        ")
        print(f" Total price: {self.total_price:.2f} €.                ")
        print(" Thank you for using our digital taxi.")
        print("----------------------------------------")

        #Adding the journey to the historical.txt file.
        self.logger(self.passenger_name, self.total_duration, self.total_price)


if __name__ == "__main__":
    #Starting infinite loop for the program.
    # while True:
    #     main()
    #     #Waiting 2 seconds before starting the next journey.
    #     time.sleep(3)
    #its comment out, to test the program.
    
    # OOP Execution Flow:
    taxi_app = Taxi()
    taxi_app.welcome_passenger()
    
    if taxi_app.continue_journey:
        taxi_app.start_journey_loop()
        taxi_app.end_journey()
