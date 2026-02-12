# Write a program to animate a face bouncing around in a window (see 
# Programming Exercises 17 from Chapter 6 and Exercise 13 from Chapter 7).
# Use a list of graphics objects to represent the face.

import graphics

### COPIED FROM CH07 EXERCISE 13 ###
def drawFace(center, size, win):
    face = []
    # Head
    head = graphics.Circle(center, size)
    head.setFill("yellow")
    head.draw(win)
    face.append(head)
    # Eyes
    leftEye = graphics.Circle(
        graphics.Point(center.getX() - size/3.0, center.getY() + size/3.0),
        size/6.0)
    leftEye.setFill("black")
    leftEye.draw(win)
    face.append(leftEye)
    rightEye = leftEye.clone()
    rightEye.move(size * 2/3, 0)
    rightEye.draw(win)
    face.append(rightEye)
    # Nose
    nose = graphics.Circle(center, size/10.0)
    nose.setFill("yellow")
    nose.draw(win)
    face.append(nose)
    # Mouth
    mouth = graphics.Circle(
        graphics.Point(center.getX(), center.getY() - size/2),
        size/6.0)
    mouth.setFill("black")
    mouth.draw(win)
    face.append(mouth)
    return face

def main():
    win = graphics.GraphWin()
    win.setCoords(-100, -100, 100, 100)

    center = graphics.Point(0, 0)
    radius = 20
    face = drawFace(center, radius, win)
    head = face[0]

    ### COPIED FROM CH06 EXERCISE 17 ###
    dx = 1
    dy = 2
    for _ in range(10000):
        if abs(head.getCenter().getX()) + head.getRadius() >= 100:
            dx = dx * -1
        if abs(head.getCenter().getY()) + head.getRadius() >= 100:
            dy = dy * -1
        for e in face:
            e.move(dx, dy)
        graphics.update(30)

    win.getMouse()
    win.close()    

main()