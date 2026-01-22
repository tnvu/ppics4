# Use your drawFace function from the previous exercise to write a photo
# anonymizer. This program allows a user to load an image file (such as a
# PPM or GIF) and to draw cartoon faces over the top of existing faces in the
# photo. The user first inputs the name of the file containing the image. The
# image is displayed and the user is asked how many faces are to be blocked.

import math
import graphics

### COPIED FROM exercise-09.py ###
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

def square(x):
    return x**2

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) 
                     + square(p2.getY() - p1.getY()))
    return dist

def main():
    # Enter filename
    filename = input("Enter filename: ")
    image = graphics.Image(graphics.Point(5, 5), filename)
    width = image.getWidth()
    height = image.getHeight()
    # Set window to size of image
    win = graphics.GraphWin("Photo Anonymizer", width, height)
    win.setCoords(0, 0, width, height)
    image = graphics.Image(graphics.Point(width/2, height/2), filename)
    image.draw(win)
    # How many faces?
    nFaces = int(input("Number of faces: "))
    for _ in range(nFaces):
        center = win.getMouse()
        edge = win.getMouse()
        drawFace(center, distance(center, edge), win)
    # Wait for mouse click
    win.getMouse()
    win.close()

main()