# In graphics applications, it is often useful to group separate pieces of
# a drawing together into a single object. For example, a face might be
# drawn from individual shapes, but then positioned as a whole group.
# Create a new class GraphicsGroup that can be used for this purpose. A
# GraphicsGroup will manage a list of graphics objects and have the following
# methods:
#       __init__(self, anchor) anchor isaPoint. Creates an empty group with
#           the given anchor point.
#       getAnchor(self) Returns a clone of the anchor point.
#       addObject(self, gObject) gObject is a graphics object. Adds gObject
#           to the group.
#       move(self, dx, dy) Moves all of the objects in the group (including the
#           anchor point).
#       draw(self, win) Draws all the objects in the group into win. The anchor
#           point is not drawn.
#       undraw(self) Undraws all the objects in the group.
# Use your new class to write a program that draws some simple picture
# with multiple components and moves it to wherever the user clicks.

import graphics

class GraphicsGroup:
    def __init__(self, anchor):
        self.anchor = anchor
        self.gObjects = []

    def getAnchor(self):
        return self.anchor
    
    def addObject(self, gObject):
        self.gObjects.append(gObject)

    def move(self, dx, dy):
        self.anchor.move(dx, dy)
        for gObject in self.gObjects:
            gObject.move(dx, dy)
        
    def draw(self, win):
        for gObject in self.gObjects:
            gObject.draw(win)

    def undraw(self):
        for gObject in self.gObjects:
            gObject.undraw()

def main():
    win = graphics.GraphWin()
    size = 75
    face = GraphicsGroup(graphics.Point(100, 100))
    head = graphics.Circle(face.getAnchor(), size)
    face.addObject(head)
    eyeOff = size / 3
    leftEye = graphics.Circle(face.getAnchor(), 0.15 * size)
    rightEye = leftEye.clone()
    leftEye.move(-eyeOff, -eyeOff)
    rightEye.move(eyeOff, -eyeOff)
    face.addObject(leftEye)
    face.addObject(rightEye)
    mouthSize = 0.8 * size
    mouthOff = size / 2
    p1 = face.getAnchor().clone()
    p2 = p1.clone()
    p1.move(-mouthSize/2, mouthOff)
    p2.move(mouthSize/2, mouthOff)
    mouth = graphics.Polygon(p1, p2)
    face.addObject(mouth)
    
    face.draw(win)
    for _ in range(10):
        pt = win.getMouse()
        dx = pt.getX() - face.getAnchor().getX()
        dy = pt.getY() - face.getAnchor().getY()
        face.move(dx, dy)

main()