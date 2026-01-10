# Modify the chaos program so that the number of values to print is determined 
# by the user. You will have to add a line near the top of the program to get
# another value from the user:
#       n = int(input("How many numbers should I print? "))
# Then you will need to change the loop to use n instead of a specific number.

def exercise05():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    n = int(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)


exercise05()