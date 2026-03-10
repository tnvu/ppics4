# Modify the Dice Poker program from this chapter to include any or all of
# the following features:
# a) Splash Screen. When the program first fires up, have it print a short
# introductory message about the program and buttons for “Let’s Play”
# and “Exit.” The main interface shouldn’t appear unless the user selects
# “Let’s Play.”
# b) Add a “Help” button that pops up another window displaying the rules of 
# the game (the payoffs table is the most important part).
# c) Add a high score feature. The program should keep track of the 10 best 
# scores. When a user quits with a good enough score, he/she is invited to 
# type in a name for the list. The list should be printed in the splash screen
# when the program first runs. The high-scores list will have to be stored in 
# a file so that it persists between program invocations.

import graphics
import random

class Dice:
    def __init__(self):
        self.dice = [0] * 5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = random.randrange(1, 7)

    def rollAll(self):
        self.roll(range(5))

    def values(self):
        return self.dice[:]
    
    def score(self):
        # Create the counts list
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1
        # score the hand
        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif 3 in counts:
            return "Three of a Kind", 8
        elif not (2 in counts) and (counts[1] == 0 or counts[6] == 0):
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        else:
            return "Garbage", 0
        
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

    def undraw(self):
        self.label.undraw()
        self.rect.undraw()

class DieView:
    """DieView is a widget that displays a graphical representation of a
    standard six-sided die.
    """

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.: d1 = GDie(myWin, Point(40,50), 20)
           creates a die centered at (40,50) having sides of length
           20.
        """
        # first define some standard values
        self.win = win
        self.background = "white"  # color of die face
        self.foreground = "black"  # color of the pips
        self.psize = 0.1 * size    # radius of each pip
        hsize = size / 2.0         # half of size
        offset = 0.6 * hsize       # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = graphics.Point(cx - hsize, cy - hsize)
        p2 = graphics.Point(cx + hsize, cy + hsize)
        rect = graphics.Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create a list of 7 circles in standard pip locations
        self.pips = []
        self._addPip(cx - offset, cy - offset)  # upper left
        self._addPip(cx - offset, cy)           # left center
        self._addPip(cx - offset, cy + offset)  # lower left
        self._addPip(cx, cy)                    # center
        self._addPip(cx + offset, cy - offset)  # upper right
        self._addPip(cx + offset, cy)           # center right
        self._addPip(cx + offset, cy + offset)  # lower right

        # Create a table saying which pips are on for each value.
        self.onTable = [[], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6],
                        [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6]]

        # start with view showing 1
        self.setValue(1)

    def _addPip(self, x, y):
        """Internal helper method to add a pip at (x,y)"""
        pip = graphics.Circle(graphics.Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        self.pips.append(pip)

    def setValue(self, value):
        """ Set this die to display value."""
        self.value = value
        # Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn the appropriate pips on
        on = self.onTable[value]
        for i in on:
            self.pips[i].setFill(self.foreground)

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)

class GraphicsInterface:
    def __init__(self):
        self.win = graphics.GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = graphics.Text(graphics.Point(300, 30), "Python Poker Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        # Splash screen
        self.msg = graphics.Text(graphics.Point(300, 200),
                                 "Welcome to video poker.")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.buttons = []
        b = Button(self.win, graphics.Point(300, 280), 400, 40, "Let's Play")
        self.buttons.append(b)
        b = Button(self.win, graphics.Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)
        self.playInitialized = False

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        
        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()     # function exit here

    def createDice(self, center, size):
        center.move(-3 * size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5 * size, 0)

    def addDiceButtons(self, center, width, height):
        center.move(-3 * width, 0)
        for i in range(1, 6):
            label = f"Die {i}"
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5 * width, 0)
    
    def setMoney(self, amt):
        self.money.setText(f"${amt}")

    def showResult(self, msg, score):
        if score > 0:
            text = f"{msg}! You win ${score}"
        else:
            text = f"You rolled {msg}"
        self.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def setupPlay(self):
        if self.playInitialized:
            return
        # Remove splash screen interface
        self.msg.undraw()
        for b in self.buttons:
            b.undraw()
        # Draw playing interface
        self.msg = graphics.Text(graphics.Point(300, 380),
                                 "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(graphics.Point(300, 100), 75)
        self.buttons = []
        self.addDiceButtons(graphics.Point(300, 170), 75, 30)
        b = Button(self.win, graphics.Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, graphics.Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, graphics.Point(30, 375), 40, 30, "Help")
        self.buttons.append(b)
        b = Button(self.win, graphics.Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = graphics.Text(graphics.Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)
        self.playInitialized = True
    
    def showHelp(self):
        helpWindow = graphics.GraphWin("Help", 400, 300)
        helpWindow.setCoords(0, 0, 10, 10)
        helpWindow.setBackground("green3")
        banner = graphics.Text(graphics.Point(4, 9), "Payout")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(helpWindow)
        payouts = [("Five of a Kind", 30),
                   ("Straight", 20),
                   ("Four of a Kind", 15),
                   ("Full House", 12),
                   ("Three of a Kind", 8),
                   ("Two Pairs", 5),
                   ("Garbage", 0)]
        for i in range(len(payouts)):
            payout = payouts[i]
            hand = graphics.Text(graphics.Point(3, i+1), payout[0])
            hand.setSize(18)
            hand.setFill("yellow2")
            hand.draw(helpWindow)
            pay = graphics.Text(graphics.Point(7, i+1), f"${payout[1]}")
            pay.setSize(18)
            pay.setFill("yellow2")
            pay.draw(helpWindow)

    def wantToPlay(self):
        ans = self.choose(["Let's Play", "Roll Dice", "Quit"])
        self.msg.setText("")
        if ans in ["Let's Play", "Roll Dice"]:
            self.setupPlay()
            return True
        return False
    
    def chooseDice(self):
        # choices is a list of the indexes of the selected dice
        choices = []             # No dice chosen yet
        while True:
            # wait for user to click a valid button
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score", "Help"])
            if b[0] == "D":             # User clicked a die button
                i = int(b[4]) - 1       # Translate label to die index
                if i in choices:        # Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:                   # Currently unselected, select it
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:                       # User clicked Roll or Score
                for d in self.dice:     # Revert appearance of all dice
                    d.setColor("black")
                if b == "Score":        # Score clicked, ignore other choices
                    return []
                elif choices != []:     # Don't accept Roll unless some
                    return choices      #   dice are actually selected
                elif b == "Help":
                    self.showHelp()
                
    def close(self):
        self.win.close()

class PokerApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()
        self.interface.close()

    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

def main():
    app = PokerApp(GraphicsInterface())
    app.run()

main()