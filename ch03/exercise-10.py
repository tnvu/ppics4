# Write a program to determine the length of a ladder required to reach a
# given height when leaned against a house. The height and angle of the
# ladder are given as inputs. To compute length use:
#       length = height / sin(angle)
# Note: The angle must be in radians. Prompt for an angle in degrees and
# use this formula to convert:
#       radians = (pi/180) * degrees

import math

def main():
    height = float(input("Enter height: "))
    angle_degrees = float(input("Degrees: "))
    angle_radians = (math.pi / 180) * angle_degrees
    length = height / math.sin(angle_radians)
    print("Length: ", length)

main()
