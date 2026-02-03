# Archery Scorer. Write a program that draws an archery target (see
# Programming Exercise 2 from Chapter 4) and allows the user to click five
# times to represent arrows shot at the target. Using five-band scoring, a
# bulls-eye (yellow) is worth 9 points and each successive ring is worth 2
# fewer points down to 1 for white. The program should output a score for
# each click and keep track of a running sum for the entire series.

import graphics
import math

def drawArcheryBand(window, color, radius):
    circle = graphics.Circle(graphics.Point(0, 0), radius)
    circle.setFill(color)
    circle.draw(window)
    return circle

def calculateDistance(p):
    x = p.getX()
    y = p.getY()
    d = math.sqrt(x**2 + y**2)
    return d

def main():
    RADIUS_WHITE  = 15
    RADIUS_BLACK  = 12
    RADIUS_BLUE   = 9
    RADIUS_RED    = 6
    RADIUS_YELLOW = 3
    SCORE_WHITE  = 1
    SCORE_BLACK  = 3
    SCORE_BLUE   = 5
    SCORE_RED    = 7
    SCORE_YELLOW = 9

    win = graphics.GraphWin()
    win.setCoords(-15, -15, 15, 15)
    drawArcheryBand(win, "white", RADIUS_WHITE)
    drawArcheryBand(win, "black", RADIUS_BLACK)
    drawArcheryBand(win, "blue", RADIUS_BLUE)
    drawArcheryBand(win, "red", RADIUS_RED)
    drawArcheryBand(win, "yellow", RADIUS_YELLOW)

    total = 0
    for _ in range(5):
        p = win.getMouse()
        d = calculateDistance(p)
        if d < RADIUS_YELLOW:
            print("Score: ", SCORE_YELLOW)
            total = total + SCORE_YELLOW
        elif d < RADIUS_RED:
            print("Score: ", SCORE_RED)
            total = total + SCORE_RED
        elif d < RADIUS_BLUE:
            print("Score: ", SCORE_BLUE)
            total = total + SCORE_BLUE
        elif d < RADIUS_BLACK:
            print("Score: ", SCORE_BLACK)
            total = total + SCORE_BLACK
        elif d < RADIUS_WHITE:
            print("Score: ", SCORE_WHITE)
            total = total + SCORE_WHITE
        else:
            print("Score: 0")

    print("Total = ", total)
    win.getMouse()
    win.close()

main()