# Write a graphical program to trace a random walk (see previous three 
# problems) in two dimensions. In this simulation you should allow the step to
# be taken in any direction. You can generate a random direction as an angle 
# off of the x axis.
#       angle = random() * 2 * math.pi
# The new x and y positions are then given by these formulas:
#       x = x + cos(angle)
#       y = y + sin(angle)
# The program should take the number of steps as an input. Start your walker 
# at the center of a 100x100 grid and draw a line that traces the walk as it
# progresses.

import graphics
import math
import random

def main():
    n = int(input("Number of steps: "))

    win = graphics.GraphWin()
    win.setCoords(-50, -50, 50, 50)
    walker = graphics.Point(0, 0)
    walker.draw(win)

    win.getMouse()
    for _ in range(n):
        angle = random.random() * 2 * math.pi
        newX = walker.getX() + math.cos(angle)
        newY = walker.getY() + math.sin(angle)
        graphics.Line(walker, graphics.Point(newX, newY)).draw(win)
        walker.move(newX - walker.getX(), newY - walker.getY())
    win.getMouse()

main()
