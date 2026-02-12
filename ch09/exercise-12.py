# Using the card representation proposed in the previous problem, write a
# set of functions that can be used to categorize five-card poker hands.
# Straight flush: Five ranks in a row, all of the same suit.
# Four of a kind: Four of the same rank.
# Full house: Three of one rank and two of another.
# Flush: Five cards of the same suit.
# Straight: Five ranks in a row.
# Three of a kind: Three of one rank (but not a full house or four of a kind).
# Two pair: Two each of two different ranks.
# Pair: Two of the same rank (but not two pair, three or four of a kind).
# For example, straightflush(cards) should return True if the list of
# cards is a straight flush. Note, due to the way Python orders tuples, if
# you sort the list, the card tuples will be arranged by rank from lowest to
# highest and grouped by suit within ranks.

import unittest

def straightflush(cards):
    # check for matching suits
    suits = [c[1] for c in cards]
    if suits.count(suits[0]) != 5:
        return False
    # check ranks in a row
    ranks = [c[0] for c in cards]
    ranks.sort()
    for i in range(len(ranks) - 1):
        if ranks[i] + 1 != ranks[i+1]:
            return False
    return True

def fourofakind(cards):
    ranks = [c[0] for c in cards]
    for r in ranks:
        if ranks.count(r) == 4:
            return True
    return False

def fullhouse(cards):
    ranks = [c[0] for c in cards]
    threes = []
    twos = []
    for r in ranks:
        if ranks.count(r) == 3 and r not in threes:
            threes.append(r)
        if ranks.count(r) == 2 and r not in twos:
            twos.append(r)
    return len(threes) == 1 and len(twos) == 1

def flush(cards):
    # check suits
    suits = [c[1] for c in cards]
    if suits.count(suits[0]) != 5:
        return False
    # check ranks are NOT sorted
    ranks = [c[0] for c in cards]
    ranks.sort()
    for i in range(len(ranks) - 1):
        if ranks[i] + 1 != ranks[i+1]:
            return True
    return False

def straight(cards):
    # check suits
    suits = [c[1] for c in cards]
    if suits.count(suits[0]) == 5:
        return False
    # check ranks are sorted
    ranks = [c[0] for c in cards]
    ranks.sort()
    for i in range(len(ranks) - 1):
        if ranks[i] + 1 != ranks[i+1]:
            return False
    return True

def threeofakind(cards):
    ranks = [c[0] for c in cards]
    threes = []
    twos = []
    for r in ranks:
        if ranks.count(r) == 3 and r not in threes:
            threes.append(r)
        if ranks.count(r) == 2 and r not in twos:
            twos.append(r)
    return len(threes) == 1 and len(twos) == 0

def twopair(cards):
    ranks = [c[0] for c in cards]
    pairs = []
    for r in ranks:
        if ranks.count(r) == 2 and r not in pairs:
            pairs.append(r)
    return len(pairs) == 2

def pair(cards):
    ranks = [c[0] for c in cards]
    pairs = []
    for r in ranks:
        c = ranks.count(r)
        if c == 2 and r not in pairs:
            pairs.append(r)
        elif c > 2:
            # Three or four of a kind
            return False
    return len(pairs) == 1

class TestCards(unittest.TestCase):
    cards_single = [(2, 'c'), (3, 'd'), (4, 'h'), (5, 's'), (7, 'c')]
    cards_pair = [(2, 'c'), (4, 'd'), (2, 'h'), (5, 's'), (7, 'c')]
    cards_two_pair = [(2, 'c'), (2, 'd'), (7, 'h'), (4, 's'), (4, 'c')]
    cards_threeofakind = [(2, 'c'), (2, 'd'), (3, 'h'), (2, 's'), (7, 'c')]
    cards_straight = [(2, 'c'), (3, 'd'), (4, 'h'), (5, 's'), (6, 'c')]
    cards_flush = [(2, 'c'), (3, 'c'), (4, 'c'), (5, 'c'), (7, 'c')]
    cards_fullhouse = [(2, 'c'), (3, 'd'), (3, 'h'), (2, 's'), (2, 'd')]
    cards_fourofakind = [(2, 'c'), (2, 'd'), (2, 'h'), (5, 's'), (2, 's')]
    cards_straightflush = [(2, 'c'), (3, 'c'), (4, 'c'), (5, 'c'), (6, 'c')]

    def testPair(self):
        self.assertFalse(pair(self.cards_single))
        self.assertTrue(pair(self.cards_pair))
        self.assertFalse(pair(self.cards_two_pair))
        self.assertFalse(pair(self.cards_threeofakind))
        self.assertFalse(pair(self.cards_straight))
        self.assertFalse(pair(self.cards_flush))
        self.assertFalse(pair(self.cards_fullhouse))
        self.assertFalse(pair(self.cards_fourofakind))
        self.assertFalse(pair(self.cards_straightflush))

    def testTwoPair(self):
        self.assertFalse(twopair(self.cards_single))
        self.assertFalse(twopair(self.cards_pair))
        self.assertTrue(twopair(self.cards_two_pair))
        self.assertFalse(twopair(self.cards_threeofakind))
        self.assertFalse(twopair(self.cards_straight))
        self.assertFalse(twopair(self.cards_flush))
        self.assertFalse(twopair(self.cards_fullhouse))
        self.assertFalse(twopair(self.cards_fourofakind))
        self.assertFalse(twopair(self.cards_straightflush))

    def testThreeofakind(self):
        self.assertFalse(threeofakind(self.cards_single))
        self.assertFalse(threeofakind(self.cards_pair))
        self.assertFalse(threeofakind(self.cards_two_pair))
        self.assertTrue(threeofakind(self.cards_threeofakind))
        self.assertFalse(threeofakind(self.cards_straight))
        self.assertFalse(threeofakind(self.cards_flush))
        self.assertFalse(threeofakind(self.cards_fullhouse))
        self.assertFalse(threeofakind(self.cards_fourofakind))
        self.assertFalse(threeofakind(self.cards_straightflush))

    def testStraight(self):
        self.assertFalse(straight(self.cards_single))
        self.assertFalse(straight(self.cards_pair))
        self.assertFalse(straight(self.cards_two_pair))
        self.assertFalse(straight(self.cards_threeofakind))
        self.assertTrue(straight(self.cards_straight))
        self.assertFalse(straight(self.cards_flush))
        self.assertFalse(straight(self.cards_fullhouse))
        self.assertFalse(straight(self.cards_fourofakind))
        self.assertFalse(straight(self.cards_straightflush))

    def testFlush(self):
        self.assertFalse(flush(self.cards_single))
        self.assertFalse(flush(self.cards_pair))
        self.assertFalse(flush(self.cards_two_pair))
        self.assertFalse(flush(self.cards_threeofakind))
        self.assertFalse(flush(self.cards_straight))
        self.assertTrue(flush(self.cards_flush))
        self.assertFalse(flush(self.cards_fullhouse))
        self.assertFalse(flush(self.cards_fourofakind))
        self.assertFalse(flush(self.cards_straightflush))

    def testFullhouse(self):
        self.assertFalse(fullhouse(self.cards_single))
        self.assertFalse(fullhouse(self.cards_pair))
        self.assertFalse(fullhouse(self.cards_two_pair))
        self.assertFalse(fullhouse(self.cards_threeofakind))
        self.assertFalse(fullhouse(self.cards_straight))
        self.assertFalse(fullhouse(self.cards_flush))
        self.assertTrue(fullhouse(self.cards_fullhouse))
        self.assertFalse(fullhouse(self.cards_fourofakind))
        self.assertFalse(fullhouse(self.cards_straightflush))

    def testFourofakind(self):
        self.assertFalse(fourofakind(self.cards_single))
        self.assertFalse(fourofakind(self.cards_pair))
        self.assertFalse(fourofakind(self.cards_two_pair))
        self.assertFalse(fourofakind(self.cards_threeofakind))
        self.assertFalse(fourofakind(self.cards_straight))
        self.assertFalse(fourofakind(self.cards_flush))
        self.assertFalse(fourofakind(self.cards_fullhouse))
        self.assertTrue(fourofakind(self.cards_fourofakind))
        self.assertFalse(fourofakind(self.cards_straightflush))

    def testStraightflush(self):
        self.assertFalse(straightflush(self.cards_single))
        self.assertFalse(straightflush(self.cards_pair))
        self.assertFalse(straightflush(self.cards_two_pair))
        self.assertFalse(straightflush(self.cards_threeofakind))
        self.assertFalse(straightflush(self.cards_straight))
        self.assertFalse(straightflush(self.cards_flush))
        self.assertFalse(straightflush(self.cards_fullhouse))
        self.assertFalse(straightflush(self.cards_fourofakind))
        self.assertTrue(straightflush(self.cards_straightflush))

if __name__ == '__main__':
    unittest.main()