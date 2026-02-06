# Write a program that graphically plots a regression line — that is, the line
# with the best fit through a collection of points. First ask the user to
# specify the data points by clicking on them in a graphics window. To find
# the end of input, place a small rectangle labeled “Done” in the lower-left
# corner of the window; the program will stop gathering points when the user
# clicks inside that rectangle.
#
# The regression line is the line with the following equation:
#       y = mean(y) + m(x — mean(x))
# where
#       m = summation(xi, yi) - n * mean(x) * mean(y)
#           ---------------------------------------
#               summation(xi^2) - n*mean(x)^2
# mean(x) is the mean of the x-values, mean(y) is the mean of the y-values,
# and n is the number of points.
#
# As the user clicks on points, the program should draw them in the graphics
# window and keep track of the count of input values and the running sum of
# x, y, x^2, and xy values. When the user clicks inside the “Done” rectangle,
# the program then computes the value of y (using the equations above)
# corresponding to the x values at the left and right edges of the window to
# compute the endpoints of the regression line spanning the window. After the
# line is drawn, the program will pause for another mouse click before closing
#  the window and quitting.

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

    n = 0
    total_x = 0
    total_y = 0
    total_xy = 0
    total_x2 = 0
    while True:
        p = win.getMouse()
        if done_p1.getX() <= p.getX() <= done_p2.getX() and \
            done_p1.getY() <= p.getY() <= done_p2.getY():
            break
        p.draw(win)

        n = n + 1
        total_x = total_x + p.getX()
        total_y = total_y + p.getY()
        total_xy = total_xy + (p.getX() * p.getY())
        total_x2 = total_x2 + p.getX()**2

    mean_x = total_x / n
    mean_y = total_y / n
    m = (total_xy - (n * mean_x * mean_y)) / (total_x2 - n * mean_x**2)
    y1 = mean_y + m * (-100 - mean_x)
    y2 = mean_y + m * (100 - mean_x)
    graphics.Line(graphics.Point(-100, y1), graphics.Point(100, y2)).draw(win)
    win.getMouse()

main()