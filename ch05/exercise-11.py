# Write a function to meet this specification.
#   moveTo(shape, newCenter) shape is a graphics object that supports the
#       getCenter method and newCenter is a Point. Moves shape so that
#       newCenter is its center.
# Use your function to write a program that draws a circle and then allows
# the user to click the window 10 times. Each time the user clicks, the circle
# is moved where the user clicked.

import graphics

def moveTo(shape, newCenter):
    oldCenter = shape.getCenter()
    dx = newCenter.getX() - oldCenter.getX()
    dy = newCenter.getY() - oldCenter.getY()
    shape.move(dx, dy)

def main():
    win = graphics.GraphWin("moveTo")
    win.setCoords(-10, -10, 10, 10)

    shape = graphics.Circle(graphics.Point(0, 0), 3)
    shape.setFill("yellow")
    shape.draw(win)

    for _ in range(10):
        p = win.getMouse()
        moveTo(shape, p)

    win.getMouse()
    win.close()

main()
