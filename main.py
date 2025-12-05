import time
import logging
import os

stopped_rate_day = 0.02
moving_rate_day = 0.05
base_rate_day = 10.0
stopped_rate_nocturne = 0.20
moving_rate_nocturne = 0.40
base_rate_nocturne = 20.0


#Clear console function.
def clear_console():

    os.system('cls' if os.name == 'nt' else 'clear')

def get_rates_from_auth():
    while True:
        password_input = input("Welcome driver Maui, insert your password to start the car: ").strip()
        if password_input != "password":
            print("Incorrect password, try again.")
            continue
        print("Correct password.")

        while True:
            time_input_str = input("Insert the current time: 0-23h format: ").strip()
            try:
                time_input = int(time_input_str)
                if 0 <= time_input <= 23:
                    if time_input >= 18 or time_input <= 6:
                        print("The nigh's young, Starting the car...")
                        return stopped_rate_nocturne, moving_rate_nocturne, base_rate_nocturne
                    else:
                        print("Wonderful day today, Starting the car...")
                        return stopped_rate_day, moving_rate_day, base_rate_day
                else:
                    print("Incorrect time, try again.")
            except ValueError:
                print("Come on, just see your watch.")


def welcome():
    clear_console()
    stopped_rate, moving_rate, base_rate = get_rates_from_auth()

    logging.warning('Starting working') 
    print(" Welcome to our digital Taxi")
    print("\n")
    print(" Welcome again! Please enter the passenger name:")
    name = input().strip()
    print("\n")
    print(f" Helloo, {name}!")
    print(f" The minimun fare is {base_rate:.2f} €.")
    print(f" The stop fare is {stopped_rate:.2f}€ per second.")
    print(f" The moving fare is {moving_rate:.2f}€ per second.")
    print("\n")
    print(" Do you wish to continue? (y/n)")
    answer = input().strip().lower()
    if answer == "y":
        print(" Great, let's go!")
        return True, name, stopped_rate, moving_rate, base_rate
    else:
        print(" We hope to see you again!")
        return False, None, stopped_rate, moving_rate, base_rate

def historical_txt(name, total_duration, total_price):
    fareContent = f"Name: {name}\n"
    fareContent += f"Total duration: {total_duration:.2f} seconds\n"
    fareContent += f"Total price: {total_price:.2f} €\n" 
    fareContent += "\n" 
    try:
        #Using "with open" to append the fare content to the historical.txt file.
        with open("historical.txt", "a",encoding='utf-8') as file:
            file.write(fareContent)
    except IOError:
        print("Error trying to write to historical.txt")
    

def main():
    continue_journey, name, stopped_rate, moving_rate, base_rate = welcome()
    
    total_duration = 0.0
    total_price = 0.0

    if continue_journey:
        total_price = base_rate
        starting_time_journey = time.time()
        starting_time_state = starting_time_journey
        # current_state = "Moving" Starting state.
        print("\n Be welcome and enjoy your journey! Current state: moving")
        print(f" Current fare: {total_price:.2f} €.")
        print(" Instructions: Use 'S' for stop, 'M' for move, and 'X' for exit.")
        logging.warning('Instructions working') 
        #Starting infinite loop for the journey.
        current_state = "moving"


        while True:
            #waiting for the user to input "  ".
            answer = input(" ").strip().lower()
            current_time = time.time()
            duration = current_time - starting_time_state

            #adding the duration to the total price.
            if current_state == "moving":
                total_price += moving_rate * duration
            else:
                total_price += stopped_rate * duration

            #resetting the starting time state.
            starting_time_state = current_time 

            if answer == "s":
                print(" Traffic lights, good heavens!!")
                current_state = "stopped"
                logging.warning('Stopped working') 

            elif answer == "m":
                print(" here we go!")
                current_state = "moving"
                logging.warning('Moving working') 

            elif answer == "x":
                print(" Lets park...")
                logging.warning('Parking working') 
                time.sleep(2)
                print(" Generating the receipt...")
                time.sleep(2)
                logging.warning('Printer working') 
                print(" Printer sound.")
                time.sleep(1)
                break
                

            else:
                print(" Ouch, Technical error! \n Try to press the right key. (S to stop, M to move, X to exit)")

            # print(f"-> Accumulated fare so far: {total_price:.2f} €")

        end_time_journey = time.time()
        total_duration = end_time_journey - starting_time_journey
        
        
        print("\n----------------------------------------")
        print("            JOURNEY SUMMARY           ")
        print("--------------------------------------")
        print(f" Total duration: {total_duration:.2f} Seconds.        ")
        print(f" Total price: {total_price:.2f} €.                ")
        print(" Thank you for using our digital taxi.")
        print("----------------------------------------")

        #Adding the journey to the historical.txt file. (MOVED INSIDE IF BLOCK)
        historical_txt(name, total_duration, total_price)

# FIX: Remove this line completely
# historical_txt(name, total_duration, total_price)

if __name__ == "__main__":
    #Starting infinite loop for the program.
    # while True:
    #     main()
    #     #Waiting 2 seconds before starting the next journey.
    #     time.sleep(3)
    #its comment out, to test the program.
    main()


# testing (This entire block should be in your tests file, not here)
# def password():
#     print("We need to know that you are a human, sorry sorry, I said a real passenger")
#     if input("Human, insert your password to start the regular taxi. \n").strip() == "password":
#         print("Beep Beep, im not a robot.")
#         return True
#     else:
#         print("You smell to oil, get out of here!")
#         return False
