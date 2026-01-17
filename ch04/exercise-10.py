# Triangle Information.
# Same as the previous problem, but with three clicks for the vertices of
# a triangle.
# Formulas:
#       For perimeter, see length from the Line Segment problem.
#       area = sqrt(s(s-a)(s-b)(s-c)) where a, b, c are the lengths of the
#           sides and s = (a + b + c) / 2

import graphics
import math

def main():
    win = graphics.GraphWin()
    win.setCoords(-10, -10, 10, 10)

    graphics.Line(graphics.Point(-10, 0), graphics.Point(10, 0)).draw(win)
    graphics.Line(graphics.Point(0, -10), graphics.Point(0, 10)).draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    triangle = graphics.Polygon(p1, p2, p3)
    triangle.draw(win)

    a = math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)
    b = math.sqrt((p3.getX() - p2.getX())**2 + (p3.getY() - p2.getY())**2)
    c = math.sqrt((p3.getX() - p1.getX())**2 + (p3.getY() - p1.getY())**2)
    s = (a + b + c) / 2
    perimeter = a + b + c
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    graphics.Text(graphics.Point(-3, -7),
                  "Perimeter = " + str(round(perimeter, 2))).draw(win)
    graphics.Text(graphics.Point(-3, -9),
                  "Area = " + str(round(area, 2))).draw(win)

    win.getMouse()
    win.close()

main()