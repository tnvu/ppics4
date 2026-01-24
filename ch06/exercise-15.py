# Do Programming Exercise 8 from Chapter 4, but add a decision to prevent
# the program from dividing by zero if the line is vertical.

import math

def main():
    x1 = float(input("X1: "))
    y1 = float(input("Y1: "))
    x2 = float(input("X2: "))
    y2 = float(input("Y2: "))

    dx = x2 - x1
    dy = y2 - y1
    midpoint_x = dx / 2
    midpoint_y = dy / 2
    slope = 'inf'
    if dx != 0:
        slope = dy / dx
    length = math.sqrt(dx**2 + dy**2)

    print("Midpoint = (" + str(midpoint_x) + ", " + str(midpoint_y) + ")")
    print("Slope = ", slope)
    print("Length = ", length)

main()