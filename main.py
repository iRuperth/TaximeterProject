#Taximeter Project

#Starting the journey.

#
import time
import os

stopped_rate = 0.2
moving_rate = 0.5
base_rate = 10

def welcome():
    print("Be welcome to our digital taxi")
    print("Could you please enter your name?")
    name = input()
    print(f"Hello {name}!")
    print(f"The base rate is {base_rate:.2f}€")
    print(f"The stopped rate is {stopped_rate:.2f}€")
    print(f"The moving rate is {moving_rate:.2f}€")
    print("Do you wish continue? (y/n)")
    answer = input()
    if answer == "y":
        print("Wohoo, lets go!")
        return True
    else:
        print("We hope to see you again!")
        return False

def journey():
    pass

def main():
    if welcome():
        journey()
        print("Wait a moment...")
        time.sleep(2)
        print("Oops, our journey has ended... for now.")
        print("Technical fault, please come back soon!")

if __name__ == "__main__":
    main()
