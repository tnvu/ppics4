# Modify the Face class from the previous problem to include a move method
# similar to other graphics objects. Using the move method, create a program
# that makes a face bounce around in a window (see Programming Exercise 17 
# from Chapter 6). Bonus: Have the face change expression each time it “hits”
# the edge of the window.

import graphics
import random

class Face:
    def __init__(self, window, center, size):
        self.window = window
        self.head = graphics.Circle(center, size)
        self.head.draw(window)
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        self.leftEye = graphics.Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = graphics.Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = graphics.Polygon(p1,p2)
        self.mouth.draw(window)
    
    def getCenter(self):
        return self.head.getCenter()
    
    def getSize(self):
        return self.head.getRadius()

    def move(self, dx, dy):
        for x in (self.head, self.leftEye, self.rightEye, self.mouth):
            x.move(dx, dy)

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
    center = graphics.Point(100, 105)
    size = 75
    face = Face(win, center, size)
    quit = Button(win, graphics.Point(175, 190), 50, 20, "QUIT")
    quit.activate()

    choices = [face.smile, face.frown, face.wink]
    dx = random.random()
    dy = random.random()
    while True:
        # Move face
        if (face.getCenter().getX() - face.getSize() <= 0) or \
            (face.getCenter().getX() + face.getSize() >= 200):
            dx = dx * -1
            random.choice(choices)()
        if (face.getCenter().getY() - face.getSize() <= 0) or \
            (face.getCenter().getY() + face.getSize() >= 200):
            dy = dy * -1
            random.choice(choices)()
        face.move(dx, dy)

        pt = win.checkMouse()
        if pt != None and quit.clicked(pt):
            break
    win.close()

main()