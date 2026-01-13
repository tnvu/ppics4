# Write a program that accepts two points (see previous problem) and 
# determines the distance between them.
#       distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

import math

def main():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    distance = abs(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    print("Distance = ", distance)

main()