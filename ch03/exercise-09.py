# Write a program to calculate the area of a triangle given the length of its
# three sides—a, b, and c—using these formulas:
#       s = (a + b + c) / 2
#       A = sqrt(s(s-a)(s-b)(s-c))

import math

def main():
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = float(input("Enter side C: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area = ", area)

main()