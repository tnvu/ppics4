# Redo Exercise 9 from Chapter 7 to get its data from a file.

import graphics
import tkinter.filedialog

def main():
    win = graphics.GraphWin()
    win.setCoords(-100, -100, 100, 100)

    n = 0
    total_x = 0
    total_y = 0
    total_xy = 0
    total_x2 = 0
    inFile = tkinter.filedialog.askopenfilename()
    with open(inFile, 'r') as f:
        for l in f:
            x = float(l.split()[0])
            y = float(l.split()[1])
            
            n = n + 1
            total_x = total_x + x
            total_y = total_y + y
            total_xy = total_xy + (x * y)
            total_x2 = total_x2 + x**2

    mean_x = total_x / n
    mean_y = total_y / n
    m = (total_xy - (n * mean_x * mean_y)) / (total_x2 - n * mean_x**2)
    y1 = mean_y + m * (-100 - mean_x)
    y2 = mean_y + m * (100 - mean_x)
    graphics.Line(graphics.Point(-100, y1), graphics.Point(100, y2)).draw(win)
    win.getMouse()

main()