# Create a class Deck that represents a deck of cards. Your class should have
# the following methods:
#       constructor Creates a new deck of 52 cards in a standard order.
#       shuffle Randomizes the order of the cards.
#       dealCard Returns a single card from the top of the deck and removes
#           the card from the deck.
#       cardsLeft Returns the number of cards remaining in the deck.
# Test your program by having it deal out a sequence of n cards from a
# shuffled deck where n is a user input. You could also use your deck object
# to implement a Blackjack simulation where the pool of cards is finite. See
# Programming Exercises 10 and 11 in Chapter 11.

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

class Deck:

    def __init__(self):
        self.cards = []
        for suit in ['c', 'd', 'h', 's']:
            for rank in range(1, 14):
                self.cards.append(PlayingCard(rank, suit))
    
    def shuffle(self):
        cards = []
        while len(self.cards) != 0:
            x = random.randrange(0, len(self.cards))
            cards.append(self.cards.pop(x))
        self.cards = cards

    def dealCard(self):
        return self.cards.pop(0)
    
    def cardsLeft(self):
        return len(self.cards)
    
def main():
    n = int(input("How many cards to deal? "))

    deck = Deck()
    deck.shuffle()
    for _ in range(n):
        print(deck.dealCard())
    print(f"Cards left: {deck.cardsLeft()}")
    
main()