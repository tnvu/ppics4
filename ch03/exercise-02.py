# Write a program that calculates the cost per square inch of a circular pizza,
# given its diameter and price. The formula for area is A = pi * r**2.

import math

def main():
    price = float(input("Cost of pizza: "))
    r = float(input("Diameter of pizza (inches): ")) / 2.0
    area = math.pi * r**2
    print("Price per square inch: ", price / area)

main()

