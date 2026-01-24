# Do Programming Exercise 7 from Chapter 4, but add a decision to handle
# the case where the line does not intersect the circle.

import math

def main():
    radius = float(input("Radius: "))
    y = float(input("Y-intercept: "))
    discriminant = radius**2 - y**2
    if discriminant < 0:
        print("Line does not intersect circle")
    elif discriminant == 0:
        print("X = ", 0)
    else:
        x = math.sqrt(discriminant)
        print("X = +/- ", x)
    
main()