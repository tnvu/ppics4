# Line Segment Information.
# This program allows the user to draw a line segment and then displays
# some graphical and textual information about the line segment.
#       Input:  Two mouse clicks for the end points of the line segment.
#       Output: Draw the midpoint of the segment in cyan.
#               Draw the line.
#               Print the length and the slope of the line.
#
#   Formulas: dx = x2 - x1
#             dy = y2 - y1
#             slope = dy/dx
#             length = sqrt(dx^2 + dy^2)

import graphics
import math

def main():
    win = graphics.GraphWin()
    win.setCoords(-100, -100, 100, 100)

    graphics.Line(graphics.Point(-100, 0), graphics.Point(100, 0)).draw(win)
    graphics.Line(graphics.Point(0, -100), graphics.Point(0, 100)).draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    line = graphics.Line(p1, p2).draw(win)
    midpoint = graphics.Circle(graphics.Point((p1.getX() + p2.getX()) / 2,
                                              (p1.getY() + p2.getY()) / 2),
                               3)
    midpoint.setFill("cyan")
    midpoint.setOutline("cyan")
    midpoint.draw(win)

    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    slope = dy / dx
    length = math.sqrt(dx**2 + dy**2)
    graphics.Text(graphics.Point(-30, -75),
                  "Slope = " + str(round(slope, 5))).draw(win)
    graphics.Text(graphics.Point(-30, -90),
                  "Length = " + str(round(length, 5))).draw(win)

    win.getMouse()
    win.close()

main()