import time
import logging

import os

stopped_rate = 0.02
moving_rate = 0.05
base_rate = 10.0

#Clear console function.
# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    # clear_console()
    logging.warning('Starting working') 
    print(" Welcome to our digital Taxi")
    print("\n")
    print(" Welcome again! Please enter your name:")
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
        return True, name
    else:
        print(" We hope to see you again!")
        return False, None

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
    continue_journey, name = welcome()
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

    #Adding the journey to the historical.txt file.
    historical_txt(name, total_duration, total_price)

if __name__ == "__main__":
    #Starting infinite loop for the program.
    # while True:
    #     main()
    #     #Waiting 2 seconds before starting the next journey.
    #     time.sleep(3)
    #its comment out, to test the program.
    main()


