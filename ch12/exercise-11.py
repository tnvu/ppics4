# Write a modified Button class that creates circular buttons. Call your class
# CButton and implement the exact same methods that are in the existing Button
# class. Your constructor should take the center of the button and its radius
# as normal parameters. Place your class in a module called cbutton.py. Test
# your class by modifying roller.py to use your buttons.

import graphics
import math
import random

class CButton:
    def __init__(self, win, center, radius, label):
        self.circle = graphics.Circle(center, radius)
        self.circle.draw(win)
        self.label = graphics.Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        center = self.circle.getCenter()
        radius = self.circle.getRadius()
        return (self.active and
                math.sqrt((center.getX() - p.getX())**2 +
                          (center.getY() - p.getY())**2) < radius)
    
    def getLabel(self):
        return self.label.getText()
    
    def activate(self):
        self.label.setFill("black")
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill("darkgrey")
        self.circle.setWidth(1)
        self.active = False


# dieview.py

class DieView:
    """DieView is a widget that displays a graphical representation of a
    standard six-sided die.
    """

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.: d1 = GDie(myWin, Point(40,50), 20)
           creates a die centered at (40,50) having sides of length
           20.
        """

        # first define some standard values
        self.win = win
        self.background = "white"  # color of die face
        self.foreground = "black"  # color of the pips
        self.psize = 0.1 * size    # radius of each pip
        hsize = size / 2.0         # half of size
        offset = 0.6 * hsize       # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = graphics.Point(cx - hsize, cy - hsize)
        p2 = graphics.Point(cx + hsize, cy + hsize)
        rect = graphics.Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create a list of 7 circles in standard pip locations
        self.pips = []
        self._addPip(cx-offset, cy-offset),  # upper left
        self._addPip(cx-offset, cy),         # left center
        self._addPip(cx-offset, cy+offset),  # lower left
        self._addPip(cx, cy),                # center
        self._addPip(cx+offset, cy-offset),  # upper right
        self._addPip(cx+offset, cy),         # center right
        self._addPip(cx+offset, cy+offset)   # lower right

        # Create a table saying which pips are on for each value.
        self.onTable = [[], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6],
                        [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6]]

        # start with view showing 1
        self.setValue(1)

    def _addPip(self, x, y):
        """Internal helper method to add a pip at (x,y)"""
        pip = graphics.Circle(graphics.Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        self.pips.append(pip)

    def setValue(self, value):
        """ Set this die to display value."""
        # Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn the appropriate pips on
        on = self.onTable[value]
        for i in on:
            self.pips[i].setFill(self.foreground)


# roller.py
# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView.

def main():

    # create the application window
    win = graphics.GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, graphics.Point(3, 7), 2)
    die2 = DieView(win, graphics.Point(7, 7), 2)
    rollButton = CButton(win, graphics.Point(5, 4), 1.75, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, graphics.Point(5, 1), 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = random.randrange(1, 7)
            die1.setValue(value1)
            value2 = random.randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()


main()