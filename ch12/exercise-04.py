# Extend the program from the previous problem by allowing the player to
# play multiple rounds and displaying the number of wins and losses. Add a
# “Quit” button for ending the game.

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

    playButton = Button(win, graphics.Point(20, 190), 40, 20, "Play")
    playButton.activate()
    quitButton = Button(win, graphics.Point(180, 190), 40, 20, "Quit")
    quitButton.activate()

    doors = []
    doors.append(Button(win, graphics.Point(50, 100), 50, 150, "Door 1"))
    doors.append(Button(win, graphics.Point(100, 100), 50, 150, "Door 2"))
    doors.append(Button(win, graphics.Point(150, 100), 50, 150, "Door 3"))

    winText = graphics.Text(graphics.Point(20, 10), "W: 0")
    winText.draw(win)
    statusText = graphics.Text(graphics.Point(100, 10), "Press Play")
    statusText.draw(win)
    lossesText = graphics.Text(graphics.Point(180, 10), "L: 0")
    lossesText.draw(win)

    winner = -1
    wins = 0
    losses = 0
    while True:
        pt = win.getMouse()
        if playButton.clicked(pt):
            playButton.deactivate()
            statusText.setText("Pick a door")
            winner = random.randrange(0, len(doors))
            for d in doors:
                d.activate()
        elif quitButton.clicked(pt):
            break
        else:
            doorClicked = False
            won = False
            for i in range(len(doors)):
                door = doors[i]
                if door.clicked(pt):
                    doorClicked = True
                    if i == winner:
                        won = True
                        break
            if doorClicked:
                for d in doors:
                    d.deactivate()
                if won:
                    wins = wins + 1
                    winText.setText(f'W: {wins}')
                    statusText.setText("WINNER")
                else:
                    losses = losses + 1
                    lossesText.setText(f'L: {losses}')
                    statusText.setText(f"LOSER (Door {winner+1})")
                playButton.activate()
    win.close()

main()