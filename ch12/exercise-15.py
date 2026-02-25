# Implement a class to represent a playing card. Your class should have the
# following methods:
#   __init__(self, rank, suit)
#       rank is an int in the range 1-13 indicating the ranks ace-king, and
#       suit is a single character “d,” “c,” “h,” or “s” indicating the suit
#       (diamonds, clubs, hearts, or spades). Create the corresponding card.
#   getRank(self) Returns the rank of the card.
#   getSuit(self) Returns the suit of the card.
#   value(self) Returns the blackjack value of a card. Ace counts as 1, face
#       cards count as 10.
#   __str__(self) Returns a string that names the card. For example, "Ace of 
#       Spades".
# Note: A method named __str__is special in Python. If asked to convert an
# object into a string, Python uses this method, if it's present. For example,
#   c = Card(1,"s")
#   print c
# will print “Ace of Spades.”
# Test your card class with a program that prints out n randomly generated
# cards and the associated Blackjack value where n is a number supplied by 
# the user.

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
    n = int(input("Number of cards to generate: "))
    for _ in range(n):
        r = random.randint(1, 13)
        s = random.choice(['c', 'd', 'h', 's'])
        c = PlayingCard(r, s)
        print(c)
    
main()