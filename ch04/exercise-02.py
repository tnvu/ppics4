# An archery target consists of a central circle of yellow surrounded by
# concentric rings of red, blue, black, and white. Each ring has the same
# width, which is the same as the radius of the yellow circle. Write a
# program that draws such a target. Hint: Objects drawn later will appear
# on top of objects drawn earlier.

import graphics

def main():
    win = graphics.GraphWin()
    win.setCoords(0,0, 30, 30)
    center = graphics.Point(15, 15)
    yellow = graphics.Circle(center, 3)
    yellow.setFill("yellow")
    red = graphics.Circle(center, 6)
    red.setFill("red")
    blue = graphics.Circle(center, 9)
    blue.setFill("blue")
    black = graphics.Circle(center, 12)
    black.setFill("black")
    white = graphics.Circle(center, 15)
    white.setFill("white")

    white.draw(win)
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)

    win.getMouse()

main()