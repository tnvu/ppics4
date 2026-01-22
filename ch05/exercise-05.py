# Redo Programming Exercise 2 from Chapter 3. Use two functions—one to
# compute the area of a pizza, and one to compute cost per square inch.

# Write a program that calculates the cost per square inch of a circular pizza,
# given its diameter and price. The formula for area is A = pi * r**2.

import math

def areaPizza(radius):
    return math.pi * radius**2

def cpiPizza(price, area):
    return price / area

def main():
    price = float(input("Price of pizza: "))
    diameter = float(input("Diameter of pizza (inches): "))
    area = areaPizza(diameter / 2.0)
    cpi = cpiPizza(price, area)
    print("Cost per inch: ", cpi)

main()