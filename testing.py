import sys

with open('output.txt', 'w') as file:
    sys.stdout = file  # Redirect output to file
    print('Geeks for geeks')

sys.stdout = sys.__stdout__  # Restore stdout



# f = open("demofile.txt", "r")

# print(f.read())
