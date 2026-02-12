# A playing card consists of a rank and a suit. It can be represented as a
# tuple of (rank, suit) where rank is an int and suit is a single-character
# string. If aces are considered the highest card, it's convenient to use 2—
# 14 to represent the ranks 2-10, jack, queen, king, ace. So (2, "c") is
# the two of clubs, and (14, "s") is the ace of spades. Write a function,
# makeDeck() that produces a list of 52 tuples representing a deck of cards.

def makeDeck():
    deck = []
    for s in ['c', 'd', 'h', 's']:
        for i in range(2, 15):
            deck.append((i, s))
    return deck