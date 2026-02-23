# Write a program to play “Three Button Monte.” Your program should draw
# three buttons labeled “Door 1,” “Door 2,” and “Door 3” in a window and
# randomly select one of the buttons (without telling the user which one
# is selected). The program then prompts the user to click on one of the
# buttons. A click on the special button is a win, and a click on one of the
# other two is a loss. You should tell the user whether they won or lost, and
# in the case of a loss, which was the correct button. Your program should be
# entirely graphical; that is, all prompts and messages should be displayed
# in the graphics window.

import graphics
import random

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = graphics.Point(self.xmin, self.ymin)
        p2 = graphics.Point(self.xmax, self.ymax)
        self.rect = graphics.Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = graphics.Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

def main():
    win = graphics.GraphWin("Three Button Monte")
    win.setCoords(0, 0, 200, 200)
 
    doors = []
    doors.append(Button(win, graphics.Point(50, 100), 50, 150, "Door 1"))
    doors.append(Button(win, graphics.Point(100, 100), 50, 150, "Door 2"))
    doors.append(Button(win, graphics.Point(150, 100), 50, 150, "Door 3"))
    for d in doors:
        d.activate()
    winner = random.randrange(0, len(doors))
    status = graphics.Text(graphics.Point(100, 190), "Pick a door")
    status.draw(win)

    doorClicked = False
    while not doorClicked:
        pt = win.getMouse()
        for i in range(len(doors)):
            door = doors[i]
            if door.clicked(pt):
                doorClicked = True
                if i == winner:
                    status.setText("WINNER")
                else:
                    status.setText(f"LOSER - DOOR {winner+1}")
                for d in doors:
                    d.deactivate()
                break
    win.getMouse()
    win.close()

main()