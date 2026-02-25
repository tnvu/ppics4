# Extend your card class from the previous problem with a draw(self,
# win, center) method that displays the card in a graphics window. Use
# your extended class to create and display a hand of five random cards.
# Hint: The easiest way to do this is to search the Internet for a free set of
# card images and use the Image object in the graphics library to display
# them.

import graphics
import random

class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = str(suit).lower()

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def value(self):
        if self.rank in (11, 12, 13):
            return 10
        return self.rank
    
    def draw(self, win, center):
        rank = None
        if self.rank == 1:
            rank = 'A'
        elif self.rank == 11:
            rank = 'J'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 13:
            rank = 'K'
        else:
            rank = str(self.rank)
        suit = self.suit.upper()
        cardText = graphics.Text(center, f'{rank}-{suit}')
        cardText.draw(win)
    
    def __str__(self):
        rank = None
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = str(self.rank)
        suit = None
        if self.suit == 'c':
            suit = "Clubs"
        elif self.suit == 'd':
            suit = "Diamonds"
        elif self.suit == 'h':
            suit = "Hearts"
        else:
            suit = "Spades"
        return f'{rank} of {suit}'

def main():
    win = graphics.GraphWin()
    for _ in range(5):
        pt = win.getMouse()
        c = PlayingCard(random.randint(1, 13), random.choice(['c', 'd', 'h', 's']))
        c.draw(win, pt)
    win.getMouse()
    win.close()

main()