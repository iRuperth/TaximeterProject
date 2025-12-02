import time
import os

stopped_rate = 0.02
moving_rate = 0.05
base_rate = 10.0

#Clear console function.
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    # clear_console()
    print("Welcome to our digital Taxi")
    print("\n")
    print("Could you please enter your name:")
    name = input().strip()
    print("\n")
    print(f"Helloo, {name}!")
    print(f"The minimun fare is {base_rate:.2f} €.")
    print(f"The stopped fare is {stopped_rate:.2f}€ per second.")
    print(f"The moving fare is {moving_rate:.2f}€ per second.")
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
        print("\nBe welcome and enjoy your journey! Current state: moving")
        print(f"Current fare: {total_price:.2f} €.")
        print("Instructions: Use 'S' for stop, 'M' for move, and 'X' for exit.")
        #Starting infinite loop for the journey.
        current_state = "moving"


        while True:
            answer = input("\n> ").strip().lower()
            #getting the current time.
            current_time = time.time()
            #getting the duration of the journey.
            duration = current_time - starting_time_state

            #adding the duration to the total price.
            if current_state == "moving":
                total_price += moving_rate * duration
            else:
                total_price += stopped_rate * duration

            #resetting the starting time state.
            starting_time_state = current_time 

            if answer == "s":
                print("Traffic lights, good heavens!!")
                current_state = "stopped"

            elif answer == "m":
                print("There we go!")
                current_state = "moving"

            elif answer == "x":
                print("Lets park...")
                break

            else:
                print("Ouch, Technical error, try to press the right key. (S to stop, M to move, X to exit)")

            # print(f"-> Accumulated fare so far: {total_price:.2f} €")

        end_time_journey = time.time()
        total_duration = end_time_journey - starting_time_journey
        
        print("\n----------------------------------------")
        print("|            JOURNEY SUMMARY           |")
        print("|--------------------------------------|")
        print(f"| Total duration: {total_duration:.2f} seconds.        |")
        print(f"| Total price: {total_price:.2f} €.                |")
        print("| Thank you for using our digital taxi.|")
        print("----------------------------------------")


if __name__ == "__main__":
    main()
