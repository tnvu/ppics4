# Write a program to animate a circle bouncing around a window. The basic
# idea is to start the circle somewhere in the interior of the window. Use
# variables dx and dy (both initialized to 1) to control the movement of the
# circle. Use a large counted loop (say 10,000 iterations), and each time
# through the loop move the circle using dx and dy. When the x-value of the
# center of the circle gets too high (it hits the edge), change dx to -1. When
# it gets too low, change dx back to 1. Use a similar approach for dy.
# Note: Your animation will probably run too fast. You can slow it down
# by using update from the graphics library with a rate parameter. For 
# example, this loop will be limited to going around at a rate of 30 times per
# second:
#       for _ in range(10000):
#           ...
#           update(30) # pause so rate is not more than 30 times a second

import graphics

def main():
    win = graphics.GraphWin()
    win.setCoords(-100, -100, 100, 100)

    circle = graphics.Circle(graphics.Point(1, 7), 3)
    circle.setFill("black")
    circle.setOutline("black")
    circle.draw(win)

    dx = 1
    dy = 1
    for _ in range(10000):
        if abs(circle.getCenter().getX()) + circle.getRadius() >= 100:
            dx = dx * -1
        if abs(circle.getCenter().getY()) + circle.getRadius() >= 100:
            dy = dy * -1
        circle.move(dx, dy)
        graphics.update(30)

    win.getMouse()
    win.close()

main()