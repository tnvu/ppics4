# Write and test a function to meet this specification.
#       drawFace(center, size, win) center is a Point, size is an int, and
#       win is a GraphWin.
# Draws a simple face of the given size in win.
# Your function can draw a simple smiley (or grim) face. Demonstrate the
# function by writing a program that draws several faces of varying size in a
# single window.

import graphics

def drawFace(center, size, win):
    # Head
    head = graphics.Circle(center, size)
    head.setFill("yellow")
    head.draw(win)
    # Eyes
    leftEye = graphics.Circle(
        graphics.Point(center.getX() - size/3.0, center.getY() + size/3.0),
        size/6.0)
    leftEye.setFill("black")
    leftEye.draw(win)
    rightEye = leftEye.clone()
    rightEye.move(size * 2/3, 0)
    rightEye.draw(win)
    # Nose
    nose = graphics.Circle(center, size/10.0)
    nose.setFill("yellow")
    nose.draw(win)
    # Mouth
    mouth = graphics.Circle(
        graphics.Point(center.getX(), center.getY() - size/2),
        size/6.0)
    mouth.setFill("black")
    mouth.draw(win)

def main():
    win = graphics.GraphWin()
    win.setCoords(0, 0, 10, 10)
    for i in range(2, 5):
        p = win.getMouse()
        drawFace(p, i, win)
    win.getMouse()
    win.close()

main()