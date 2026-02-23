# Use the Button class discussed in this chapter to build a GUI for one (or
# more) of your projects from previous chapters.

# button.py

import graphics


class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = graphics.Point(self.xmin, self.ymin)
        p2 = graphics.Point(self.xmax, self.ymax)
        self.rect = graphics.Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = graphics.Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False


### COPIED FROM CH11 Exercise-17 ###

import math
import random

def main():
    n = int(input("Number of steps: "))

    win = graphics.GraphWin()
    win.setCoords(-50, -50, 50, 50)
    walker = graphics.Point(0, 0)
    walker.draw(win)

    startButton = Button(win, graphics.Point(-40, 40), 20, 10, "Start")
    startButton.activate()
    quitButton = Button(win, graphics.Point(40, 40), 20, 10, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if startButton.clicked(pt):
            startButton.deactivate()
            for _ in range(n):
                angle = random.random() * 2 * math.pi
                newX = walker.getX() + math.cos(angle)
                newY = walker.getY() + math.sin(angle)
                graphics.Line(walker, graphics.Point(newX, newY)).draw(win)
                walker.move(newX - walker.getX(), newY - walker.getY())
            quitButton.activate()
        pt = win.getMouse()
    win.close()

main()
