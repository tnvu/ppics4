# Two points in a plane are specified using the coordinates (x1,y1) and
# (x2,y2). Write a program that calculates the slope of a line through two
# (non-vertical) points entered by the user.
#       slope = y2—yl
#               ------
#               x2—xl

def main():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    slope = (y2 - y1) / (x2 - x1)
    print("Slope = ", slope)

main()