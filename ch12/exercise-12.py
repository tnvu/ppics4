# Modify the DieView class from the chapter by adding a method that allows
# the color of the pips to be specified.
#       setColor(self, color) Changes the color of the pips to color.
# Hints: You can change the color by changing the value of the instance
# variable foreground, but you also need to redraw the die after doing this.
# Modify setValue so that it remembers the value of the die in an instance
# variable. Then setColor can call setValue and pass the stored value to
# redraw the die. You can test your new class with the roller.py program.
# Have the dice change to a random color after each roll (you can generate
# a random color with the color rgb function).

# dieview.py

import graphics
import random

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
        
        self._value = value

    def setColor(self, color):
        self.foreground = color
        self.setValue(self._value)


# button.py

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
    rollButton = Button(win, graphics.Point(5, 4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, graphics.Point(5, 1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = random.randrange(1, 7)
            die1.setValue(value1)
            die1.setColor(graphics.color_rgb(random.randint(0, 255),
                                             random.randint(0, 255),
                                             random.randint(0, 255)))
            value2 = random.randrange(1, 7)
            die2.setValue(value2)
            die2.setColor(graphics.color_rgb(random.randint(0, 255),
                                             random.randint(0, 255),
                                             random.randint(0, 255)))

            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()


main()