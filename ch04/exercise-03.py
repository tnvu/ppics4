# Write a program that draws some sort of face.

import graphics

def main():
    win = graphics.GraphWin()

    leftEye = graphics.Circle(graphics.Point(66, 25), 20)
    leftEye.draw(win)
    rightEye = leftEye.clone()
    rightEye.move(66, 0)
    rightEye.draw(win)

    nose = graphics.Circle(graphics.Point(100, 100), 10)
    nose.draw(win)

    mouth = graphics.Line(graphics.Point(66, 150),
                          graphics.Point(132, 150))
    mouth.draw(win)

    win.getMouse()

main()    
    