# Modify the convert.py program (Section 2.2) so that it computes and prints a
# table of Celsius temperatures and the Fahrenheit equivalents every 10 
# degrees from 0 degrees Celsius to 100 degrees Celsius.

def main():
    print("  C       F")
    for i in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        celsius = float(i)
        fahrenheit = 9/5 * celsius + 32
        print(celsius, "    ", fahrenheit)

main()