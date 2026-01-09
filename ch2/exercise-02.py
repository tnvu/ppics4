# On many systems with Python, it is possible to run a program by simply
# clicking (or double-clicking) on the icon of the program file. If you are
# able to run the convert.py program this way, you may discover another
# usability issue. The program starts running in a new window, but as soon
# as the program has finished, the window disappears so that you cannot
# read the results. Add an input statement at the end of the program so
# that it pauses to give the user a chance to read the results. Something like
# this should work:
#       input ("Press the <Enter> key to quit.")

def main():
    print("This progrm converts Celsius temps to Fahrenheit")
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit")
    input ("Press the <Enter> key to quit.")

main()