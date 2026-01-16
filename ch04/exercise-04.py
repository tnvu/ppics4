# Write a program that draws a winter scene with a Christmas tree and a
# snowman

import graphics

def main():
    win = graphics.GraphWin()

    hat = graphics.Rectangle(graphics.Point(65, 20),
                             graphics.Point(85, 40))
    hat.setFill("black")
    hat.draw(win)
    head = graphics.Circle(graphics.Point(75, 50), 10)
    head.draw(win)
    body = graphics.Circle(graphics.Point(75, 80), 20)
    body.draw(win)
    legs = graphics.Circle(graphics.Point(75, 130), 30)
    legs.draw(win)

    tree = graphics.Polygon(graphics.Point(150, 40),
                            graphics.Point(125, 130),
                            graphics.Point(175, 130))
    tree.setOutline("green")
    tree.setFill("green")
    tree.draw(win)
    trunk = graphics.Rectangle(graphics.Point(135, 130),
                               graphics.Point(165, 160))
    trunk.setOutline("brown")
    trunk.setFill("brown")
    trunk.draw(win)

    win.getMouse()
    win.close()

main()