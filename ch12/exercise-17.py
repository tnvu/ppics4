# Write a program that creates a list of card objects (see preceding exercises)
# and prints out the cards grouped by suit and in rank order within suit. Your
# program should read the list of cards from a file, where each line in the
# file represents a single card with the rank and suit separated by a space.
# Hint: First sort by rank and then by suit.

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
    cards = []
    filename = input("Enter filename: ")
    with open(filename, 'r') as infile:
        for l in infile:
            rank, suit = l.split(maxsplit=2)
            rank = int(rank)
            suit = suit.lower()
            card = PlayingCard(rank, suit)
            cards.append(card)
    cards = [(c.getSuit(), c.getRank(), i, c) for i, c in enumerate(cards)]
    cards.sort()
    cards = [c for suit, rank, i, c in cards]
    for c in cards:
        print(c)

main()

# import random
# for _ in range(20):
#     rank = random.randint(1, 13)
#     suit = random.choice(['c', 'd', 'h', 's'])
#     print(f'{rank} {suit}')
