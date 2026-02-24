# Write a class to represent spheres. Your class should implement the following methods:
#       __init__(self, radius) Creates a sphere having the given radius.
#       getRadius(self) Returns the radius of this sphere.
#       surfaceArea(self) Returns the surface area of the sphere.
#       volume (self) Returns the volume of the sphere.
# Use your new class to solve Programming Exercise 1 from Chapter 3.

import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def surfaceArea(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return 4.0 / 3.0 * math.pi * self.radius ** 3

# Write a program to calculate the volume and surface area of a sphere from
# its radius, given as input. Here are some formulas that might be useful:
#       V = 4/3 * pi * r^3
#       A = 4 * pi * r^2

def main():
    r = float(input("Enter radius: "))
    s = Sphere(r)
    print("Volume: ", s.volume(), ", Area: ", s.surfaceArea())

main()