# Rectangle Information.
# This program displays information about a rectangle drawn by the user.
#       Input: Two mouse clicks for the opposite corners of a rectangle.
#       Output: Draw the rectangle.
#               Print the perimeter and area of the rectangle.
# Formulas: area = (length)(width)
#           perimeter = 2(length + width)

import graphics

def main():
    win = graphics.GraphWin()
    win.setCoords(-10, -10, 10, 10)
    graphics.Line(graphics.Point(-10, 0), graphics.Point(10, 0)).draw(win)
    graphics.Line(graphics.Point(0, -10), graphics.Point(0, 10)).draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()

    r = graphics.Rectangle(p1, p2)
    r.draw(win)

    length = abs(p1.getY() - p2.getY())
    width = abs(p1.getX() - p2.getX())
    area = length * width
    perimeter = 2 * (length + width)
    graphics.Text(graphics.Point(-3, -7),
                  "Area = " + str(round(area, 2))).draw(win)
    graphics.Text(graphics.Point(-3, -8.5),
                  "Perimeter = " + str(round(perimeter, 2))).draw(win)

    win.getMouse()
    win.close()

main()