# Circle Intersection.
# Write a program that computes the intersection of a circle with a horizontal
# line and displays the information textually and graphically.
#   Input: Radius of the circle and the y-intercept of the line.
#   Output: Draw a circle centered at (0, 0) with the given radius in a window
#       with coordinates running from -10,-10 to 10,10.
#       Draw a horizontal line across the window with the given y-intercept.
#       Draw the two points of intersection in red.
#       Print out the z values of the points of intersection.
# Formula: x = +- sqrt(r^2 - y^2)

import graphics
import math

def main():
    win = graphics.GraphWin()
    win.setCoords(-10.0, -10.0, 10.0, 10.0)

    graphics.Line(graphics.Point(0, 10), graphics.Point(0, -10)).draw(win)
    graphics.Line(graphics.Point(-10, 0), graphics.Point(10, 0)).draw(win)
    for i in range(-10, 11):
        graphics.Line(graphics.Point(i, -0.2),
                      graphics.Point(i, 0.2)).draw(win)
        graphics.Line(graphics.Point(-0.2, i),
                      graphics.Point(0.2, i)).draw(win)

    graphics.Text(graphics.Point(-7, 9), "Radius:").draw(win)
    input_radius = graphics.Entry(graphics.Point(-2.5, 9), 3)
    input_radius.setText("1.0")
    input_radius.draw(win)
    graphics.Text(graphics.Point(-6, 7), "     Y:").draw(win)
    input_y = graphics.Entry(graphics.Point(-2.5, 7), 3)
    input_y.setText("0.0")
    input_y.draw(win)
    graphics.Text(graphics.Point(3, 9), "Draw").draw(win)
    win.getMouse()
    
    radius = float(input_radius.getText())
    y = float(input_y.getText())

    circle = graphics.Circle(graphics.Point(0, 0), radius)
    circle.setOutline("blue")
    circle.draw(win)
    line = graphics.Line(graphics.Point(-10, y),
                         graphics.Point(10, y))
    line.setOutline("red")
    line.draw(win)

    x = abs(math.sqrt(radius**2 - y**2))
    graphics.Text(graphics.Point(0, -9), "x = +/-" + str(x)).draw(win)

    win.getMouse()
    win.close()

main()