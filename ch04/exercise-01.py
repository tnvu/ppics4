# 1. Alter the program from the last discussion question in the following ways:
# (a) Make it draw squares instead of circles.
# (b) Have each successive click draw an additional square on the screen
#     (rather than moving the existing one).
# (c) Print a message on the window “Click again to quit” after the loop,
#     and wait for a final click before closing the window.

import graphics

def main():
    win = graphics.GraphWin()
    shape = graphics.Rectangle(graphics.Point(50, 50),
                               graphics.Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        s = shape.clone()
        s.move(dx, dy)
        s.draw(win)
    graphics.Text(graphics.Point(100, 100), "Click Again To Quit").draw(win)
    win.getMouse()
    win.close()

main()