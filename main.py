import time
import os

stopped_rate = 0.02
moving_rate = 0.05
base_rate = 10.0

#Clear console function.
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    clear_console()
    print("Welcome to our digital Taxi")
    print("Could you please enter your name")
    name = input().strip()
    print(f"Hello, {name}!")
    print(f"The base rate is {base_rate:.2f} €.")
    print(f"The stopped rate is {stopped_rate:.2f}€ per second.")
    print(f"The moving rate is {moving_rate:.2f}€ per second.")
    print("Do you wish to continue? (y/n)")
    answer = input().strip().lower()
    if answer == "y":
        print("Great, let's go!")
        return True
    else:
        print("We hope to see you again!")
        return False


def main():
    if welcome():
        total_price = base_rate
        starting_time_journey = time.time()
        starting_time_state = starting_time_journey
        # current_state = "Moving" Starting state.
        print("\nBe welcome and enjoy your journey! Current state: Moving")
        print(f"Current fare: {total_price:.2f} €.")
        print("Instructions: Use 'X' for exit.")
        
        #Starting infinite loop for the journey.
        while True:
            answer = input("> ").strip().lower()

            #getting the current time.
            current_time = time.time()
            #getting the duration of the journey.
            duration = current_time - starting_time_state
            #adding the duration to the total price.
            total_price += moving_rate * duration
            #resetting the starting time state.
            starting_time_state = current_time 

            if answer == "x":
                print("-> Ending journey...")
                break
            else:
                print("Invalid command. Use X to exit.")

            print(f"-> Accumulated fare so far: {total_price:.2f} €")

        end_time_journey = time.time()
        total_duration = end_time_journey - starting_time_journey
        
        print("\n----------------------------------------")
        print("            JOURNEY SUMMARY              ")
        print("----------------------------------------")
        print(f"Total duration: {total_duration:.2f} seconds")
        print(f"Total price: {total_price:.2f} €")
        print("Thank you for using our digital taxi.")
        print("----------------------------------------")

if __name__ == "__main__":
    main()
