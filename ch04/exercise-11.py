# Five-click House.
# You are to write a program that allows the user to draw a simple house
# using five mouse clicks. The first two clicks will be the opposite corners
# of the rectangular frame of the house. The third click will indicate the
# center of the top edge of a rectangular door. The door should have a total
# width that is 1/5 of the width of the house frame. The sides of the door
# should extend from the corners of the top down to the bottom of the frame.
# The fourth click will indicate the center of a square window. The window is
# half as wide as the door. The last click will indicate the peak of the roof.
# The edges of the roof will extend from the point at the peak to the corners
# of the top edge of the house frame.

import graphics

def main():
    win = graphics.GraphWin()
    win.setCoords(-10, -10, 10, 10)

    # House
    p1 = win.getMouse()
    p2 = win.getMouse()
    graphics.Rectangle(p1, p2).draw(win)
    # Door
    p3 = win.getMouse()
    house_width = abs(p1.getX() - p2.getX())
    door_width = house_width / 5
    graphics.Rectangle(
        graphics.Point(p3.getX() - door_width/2, p3.getY()),
        graphics.Point(p3.getX() + door_width/2, p1.getY())).draw(win)
    # Window
    p4 = win.getMouse()
    window_width = door_width / 2
    graphics.Rectangle(
        graphics.Point(p4.getX() - window_width/2,
                       p4.getY() + window_width/2),
        graphics.Point(p4.getX() + window_width/2,
                       p4.getY() - window_width/2)).draw(win)
    # Roof
    p5 = win.getMouse()
    graphics.Line(p5, p2).draw(win)
    graphics.Line(p5, graphics.Point(p1.getX(), p2.getY())).draw(win)

    win.getMouse()
    win.close()

main()