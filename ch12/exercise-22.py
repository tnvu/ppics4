# Redo the regression problem from Chapter 7 (Programming Exercise 9)
# using a Regression class. Your new class will keep track of the various
# quantities that are needed to compute a line of regression (the running
# sums of x, y, x^2, and xy). The Regression class should have the following
# methods:
#       _init__ Creates a new regression object to which points can be added.
#       addPoint Adds a point to the regression object.
#       predict Accepts a value of x as a parameter, and returns the value of
#           the corresponding y on the line of best fit.
# Note: Your class might also use some internal helper methods to do such
# things as compute the slope of the regression line.

class Regression:

    def __init__(self):
        self.nPoints = 0
        self.sum_x = 0
        self.sum_y = 0
        self.sum_xy = 0
        self.sum_xsquared = 0


    def addPoint(self, pt):
        self.nPoints = self.nPoints + 1
        self.sum_x = self.sum_x + pt.getX()
        self.sum_y = self.sum_y + pt.getY()
        self.sum_xy = self.sum_xy + (pt.getX() * pt.getY())
        self.sum_xsquared = self.sum_xsquared + (pt.getX() ** 2)
    
    def predict(self, x):
        mean_y = self.sum_y / self.nPoints
        mean_x = self.sum_x / self.nPoints
        m = (self.sum_xy - self.nPoints * mean_x * mean_y) \
            / (self.sum_xsquared - self.nPoints * mean_x**2)
        return mean_y + m * (x - mean_x)
    
import graphics

def main():
    win = graphics.GraphWin()
    win.setCoords(-100, -100, 100, 100)
    done_p1 = graphics.Point(-100, -100)
    done_p2 = graphics.Point(-50, -85)
    done = graphics.Rectangle(done_p1, done_p2)
    done.setWidth(1)
    done.setOutline("black")
    done.draw(win)
    done_text = graphics.Text(graphics.Point((done_p1.getX() + done_p2.getX())/2,
                                             (done_p1.getY() + done_p2.getY())/2),
                                             "DONE")
    done_text.draw(win)

    regression = Regression()
    while True:
        p = win.getMouse()
        if done_p1.getX() <= p.getX() <= done_p2.getX() and \
            done_p1.getY() <= p.getY() <= done_p2.getY():
            break
        p.draw(win)

        regression.addPoint(p)
    graphics.Line(graphics.Point(-100, regression.predict(-100)),
                  graphics.Point(100, regression.predict(100))).draw(win)
    win.getMouse()

main()