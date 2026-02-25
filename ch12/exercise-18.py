# Extend the previous program to analyze a list of five cards as a poker hand.
# After printing the cards, the program categorizes accordingly.
# Royal flush 10, jack, queen, king, ace, all of the same suit.
# Straight flush Five ranks in a row, all of the same suit.
# Four of a kind Four of the same rank.
# Full house Three of one rank and two of another.
# Flush Five cards of the same suit.
# Straight Five ranks in a row.
# Three of a kind Three of one rank (but not a full house or four of a kind).
# Two pair Two each of two different ranks.
# Pair Two of the same rank (but not two pair, three or four of a kind).
# X high If none of the previous categories fit, X is the value of the highest
# rank. For example, if the largest rank is 11, the hand is ‘Jack high.”

import unittest

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
    
def analyzeHand(hand):
    r = [c.getRank() for c in hand]
    r.sort()
    s = [c.getSuit() for c in hand]
    
    if r == [1, 10, 11, 12, 13] and s.count(s[0]) == 5:
        return "Royal flush"
    straight = [r[0] + i for i, rank in enumerate(r)]
    if r == straight and s.count(s[0]) == 5:
        return "Straight flush"
    for v in r:
        if r.count(v) == 4:
            return "Four of a kind"
    if (r[0] == r[1] == r[2] and r[3] == r[4]) or \
        (r[0] == r[1] and r[2] == r[3] == r[4]):
        return "Full house"
    if s.count(s[0]) == 5:
        return "Flush"
    if r == straight:
        return "Straight"
    if (r[0] == r[1] == r[2]) or (r[2] == r[3] == r[4]):
        return "Three of a kind"
    if (r[0] == r[1] and r[2] == r[3]) or \
        (r[0] == r[1] and r[3] == r[4]) or \
        (r[1] == r[2] and r[3] == r[4]):
        return "Two pair"
    if (r[0] == r[1]) or (r[1] == r[2]) or (r[2] == r[3]) or (r[3] == r[4]):
        return "Pair"
    high = r[-1]
    if r[0] == 1:
        high = 1
    if high == 1:
        return "Ace high"
    elif high == 11:
        return "Jack high"
    elif high == 12:
        return "Queen high"
    elif high == 13:
        return "King high"
    else:
        return f'{high} high'

class AnalyzeHandTest(unittest.TestCase):
    def testAnalyzeHand(self):
        royalFlush = [PlayingCard(1, 'S'),
                      PlayingCard(10, 'S'),
                      PlayingCard(11, 'S'),
                      PlayingCard(12, 'S'),
                      PlayingCard(13, 'S')]
        straightFlush = [PlayingCard(7, 'H'),
                         PlayingCard(8, 'H'),
                         PlayingCard(9, 'H'),
                         PlayingCard(10, 'H'),
                         PlayingCard(11, 'H')]
        fourOfAKind = [PlayingCard(8, 'C'),
                       PlayingCard(8, 'D'),
                       PlayingCard(8, 'H'),
                       PlayingCard(8, 'S'),
                       PlayingCard(11, 'H')]
        fullHouse = [PlayingCard(2, 'C'),
                     PlayingCard(2, 'H'),
                     PlayingCard(2, 'S'),
                     PlayingCard(4, 'D'),
                     PlayingCard(4, 'S')]
        flush = [PlayingCard(2, 'D'),
                 PlayingCard(5, 'D'),
                 PlayingCard(10, 'D'),
                 PlayingCard(11, 'D'),
                 PlayingCard(13, 'D')]
        straight = [PlayingCard(8, 'H'),
                    PlayingCard(9, 'D'),
                    PlayingCard(10, 'S'),
                    PlayingCard(11, 'C'),
                    PlayingCard(12, 'S')]
        threeOfAKind = [PlayingCard(7, 'C'),
                        PlayingCard(7, 'D'),
                        PlayingCard(7, 'H'),
                        PlayingCard(10, 'S'),
                        PlayingCard(11, 'S')]
        twoPair = [PlayingCard(2, 'C'),
                   PlayingCard(2, 'D'),
                   PlayingCard(7, 'S'),
                   PlayingCard(8, 'C'),
                   PlayingCard(8, 'D')]
        pair = [PlayingCard(1, 'S'),
                PlayingCard(6, 'D'),
                PlayingCard(6, 'H'),
                PlayingCard(10, 'C'),
                PlayingCard(13, 'C')]
        aceHigh = [PlayingCard(1, 'S'),
                   PlayingCard(4, 'C'),
                   PlayingCard(7, 'S'),
                   PlayingCard(10, 'H'),
                   PlayingCard(13, 'S')]
        self.assertEqual("Royal flush", analyzeHand(royalFlush))
        self.assertEqual("Straight flush", analyzeHand(straightFlush))
        self.assertEqual("Four of a kind", analyzeHand(fourOfAKind))
        self.assertEqual("Full house", analyzeHand(fullHouse))
        self.assertEqual("Flush", analyzeHand(flush))
        self.assertEqual("Straight", analyzeHand(straight))
        self.assertEqual("Three of a kind", analyzeHand(threeOfAKind))
        self.assertEqual("Two pair", analyzeHand(twoPair))
        self.assertEqual("Pair", analyzeHand(pair))
        self.assertEqual("Ace high", analyzeHand(aceHigh))

    
if __name__ == '__main__':
    unittest.main()