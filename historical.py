#total_duration
#total_price
#name
#time

import sys

from main import main

with open("historical.txt", "w") as file:
    file.write("total_duration \n")
    file.write("total_price \n")
    file.write("name \n")
    file.write("time \n")

with open("historical.txt") as file:
    for line in file:
        print(line)
