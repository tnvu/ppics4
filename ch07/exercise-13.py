# Modify the circle bouncing program (Exercise 17 from Chapter 6) so that
# it keeps running until the user presses the q key. While you are at it, add
# keyboard interactions that allow the user to change the color and speed of
# the circle.

### COPIED FROM CH06 EXERCISE 17 ###
import graphics

def main():
    win = graphics.GraphWin()
    win.setCoords(-100, -100, 100, 100)

    circle = graphics.Circle(graphics.Point(1, 7), 3)
    circle.setFill("black")
    circle.setOutline("black")
    circle.draw(win)

    dx = 1
    dy = 1
    while True:
        key = win.checkKey()
        if key == "q":
            break
        elif key == "Up":
            dx = dx * 1.1
            dy = dy * 1.1
        elif key == "Down":
            dx = dx * 0.9
            dy = dy * 0.9
        elif key == "r":
            circle.setFill("red")
        elif key == "b":
            circle.setFill("blue")
        elif key == "g":
            circle.setFill("green")

        if abs(circle.getCenter().getX()) + circle.getRadius() >= 100:
            dx = dx * -1
        if abs(circle.getCenter().getY()) + circle.getRadius() >= 100:
            dy = dy * -1
        circle.move(dx, dy)
        graphics.update(60)

    win.close()

main()