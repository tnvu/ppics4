# Here is a simple class that draws a (grim) face in a graphics window:
#
# face.py
# from graphics import *
#
# class Face:
#     def __init__(self, window, center, size):
#         eyeSize = 0.15 * size
#         eyeOff = size / 3.0
#         mouthSize = 0.8 * size
#         mouthOff = size / 2.0
#         self.head = graphics.Circle(center, size)
#         self.head.draw(window)
#         self.leftEye = graphics.Circle(center, eyeSize)
#         self.leftEye.move(-eyeOff, -eyeOff)
#         self.rightEye = graphics.Circle(center, eyeSize)
#         self.rightEye.move(eyeOff, -eyeOff)
#         self.leftEye.draw(window)
#         self.rightEye.draw(window)
#         p1 = center.clone()
#         p1.move(-mouthSize/2, mouthOff)
#         p2 = center.clone()
#         p2.move(mouthSize/2, mouthOff)
#         self.mouth = graphics.Line(p1,p2)
#         self.mouth.draw(window)
# Add methods to this class that cause the face to change expression. For
# example you might add methods such as smile, wink, frown, flinch, etc.
# Your class should implement at least three such methods.
# Use your class to write a program that draws a face and provides the
# user with buttons to change the facial expression.

import graphics

class Face:
    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = graphics.Circle(center, size)
        self.head.draw(window)
        self.leftEye = graphics.Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = graphics.Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = graphics.Polygon(p1,p2)
        self.mouth.draw(window)
        self.window = window

    def smile(self):
        self.mouth.undraw()
        points = self.mouth.getPoints()
        p1 = points[0]
        p2 = points[-1]
        midpoint = graphics.Point((p1.getX() + p2.getX()) / 2,
                                  p1.getY() + 10)
        self.mouth = graphics.Polygon(p1, midpoint, p2)
        self.mouth.draw(self.window)
        
    def frown(self):
        self.mouth.undraw()
        points = self.mouth.getPoints()
        p1 = points[0]
        p2 = points[-1]
        midpoint = graphics.Point((p1.getX() + p2.getX()) / 2,
                                  p1.getY() - 10)
        self.mouth = graphics.Polygon(p1, midpoint, p2)
        self.mouth.draw(self.window)

    def wink(self):
        self.leftEye.setFill("black")

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


def main():
    win = graphics.GraphWin("Exercise 20", 200, 200)
    face = Face(win, graphics.Point(100, 105), 75)
    smile = Button(win, graphics.Point(25, 10), 50, 20, "Smile")
    smile.activate()
    frown = Button(win, graphics.Point(100, 10), 50, 20, "Frown")
    frown.activate()
    wink = Button(win, graphics.Point(175, 10), 50, 20, "Wink")
    wink.activate()
    quit = Button(win, graphics.Point(175, 190), 50, 20, "QUIT")
    quit.activate()

    while True:
        pt = win.getMouse()
        if quit.clicked(pt):
            break
        elif smile.clicked(pt):
            face.smile()
        elif frown.clicked(pt):
            face.frown()
        elif wink.clicked(pt):
            face.wink()
    win.close()


main()