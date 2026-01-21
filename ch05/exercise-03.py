# Write definitions for these functions:
#   sphereArea(radius) Returns the surface area of a sphere having the
#       given radius.
#   sphereVolume (radius) Returns the volume of a sphere having the given
#       radius.
#  Use your functions to solve Programming Exercise 1 from Chapter 3.

import math

def sphereArea(radius):
    return 4.0 * math.pi * radius**2

def sphereVolume(radius):
    return 4.0 / 3.0 * math.pi * radius**3

def main():
    radius = float(input("Enter radius: "))
    print("Volume:", sphereVolume(radius), ", Area:", sphereArea(radius))

main()