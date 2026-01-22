# Write a function that computes the area of a triangle given the length of its
# three sides as parameters (see Programming Exercise 9 from Chapter 3).
# Use your function to augment triangle2.py from this chapter so that it
# also displays the area of the triangle.

import math

def areaTriangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Program: triangle2.py
import graphics

def square(x):
    return x**2

def distance(p1, p2):
    dist = math.sqrt(square(p1.getX() - p2.getX())
                     + square(p1.getY() - p2.getY()))
    return dist

def main():
    win = graphics.GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = graphics.Text(graphics.Point(5, 0.5), "Click on three points")
    message.draw(win)
    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    # Use Polygon object to draw the triangle
    triangle = graphics.Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)
    # Calculate the perimeter and area of the triamgle
    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    area = areaTriangle(distance(p1, p2), distance(p2, p3), distance(p3, p1))
    message.setText("Perimeter=" + str(round(perim, 2))
                    + ", Area= " + str(round(area, 2)))
    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
