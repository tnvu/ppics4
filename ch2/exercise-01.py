# A user-friendly program should print an introduction that tells the user
# what the program does. Modify the convert.py program (Section 2.2) to print 
# an introduction.

def main():
    print("This progrm converts Celsius temps to Fahrenheit")
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit")

main()