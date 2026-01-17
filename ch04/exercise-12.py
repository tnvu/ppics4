# Five-click Scarecrow.
# Write a program that allows a user to draw a scarecrow face using five mouse
# clicks. The face to be drawn has a circular head, triangle nose, circular
# eyes, and an oval for a mouth. The position and sizing of each of these
# elements is controlled by the mouse clicks made by the user.
# The first click is the center of the head and also serves as the top of the
# nose. The second click is the edge of the head. The third click is the
# lowerleft corner of the (isosceles triangle) nose. The fourth click is the
# center of the left eye. The eyes are placed symmetrically with a radius
# equal to one-tenth the radius of the head. The final click is the lower-left
# corner of the mouth’s oval. The mouth is centered horizontally and the
# height of the oval is the same as the radius of the eyes. Here’s an example
# result:

import graphics
import math

def main():
    win = graphics.GraphWin()
    win.setCoords(-10, -10, 10, 10)

    # Head
    p1 = win.getMouse()
    p2 = win.getMouse()
    head_radius = math.sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)
    head = graphics.Circle(p1, head_radius)
    head.setFill("yellow")
    head.draw(win)
    # Nose
    p3 = win.getMouse()
    nose_width = 2 * abs(p3.getX() - p1.getX())
    nose = graphics.Polygon(p1,
                            p3,
                            graphics.Point(p3.getX() + nose_width, p3.getY()))
    nose.setFill("red")
    nose.draw(win)
    # Eyes
    p4 = win.getMouse()
    left_eye = graphics.Circle(p4, head_radius/10)
    left_eye.setFill("black")
    left_eye.draw(win)
    right_eye = left_eye.clone()
    right_eye.move(2 * abs(p4.getX() - p1.getX()), 0)
    right_eye.draw(win)
    # Mouth
    p5 = win.getMouse()
    mouth_width = 2 * abs(p1.getX() - p5.getX())
    mouth = graphics.Oval(
        p5, graphics.Point(p5.getX() + mouth_width,
                           p5.getY() + left_eye.getRadius()))
    mouth.setFill("grey")
    mouth.draw(win)

    graphics.Text(graphics.Point(0, -9), "Click anywhere to quit").draw(win)
    win.getMouse()
    win.close()

main()