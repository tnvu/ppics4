# Write a program to calculate the volume and surface area of a sphere from
# its radius, given as input. Here are some formulas that might be useful:
#       V = 4/3 * pi * r^3
#       A = 4 * pi * r^2

import math

def main():
    r = float(input("Enter radius: "))
    v = 4.0 / 3.0 * math.pi * r ** 3
    a = 4 * math.pi * r ** 2
    print("Volume: ", v, ", Area: ", a)

main()