# # Write a program that deals four bridge hands, counts how many points
# they have, and gives opening bids. You will probably need to consult a
# beginner’s guide to bridge to help you out.

import random

SUITS = ['C', 'D', 'H', 'S']
RANKS = list(range(1, 14))

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        rank = self.rank
        if rank == 1:
            srank = 'A'
        elif rank == 11:
            srank = 'J'
        elif rank == 12:
            srank = 'Q'
        elif rank == 13:
            srank = 'K'
        else:
            srank = str(rank)
        return f'{srank:>2}{self.suit}'
    
    def __lt__(self, other):
        aSuit = SUITS.index(self.suit)
        bSuit = SUITS.index(other.suit)
        if aSuit == bSuit:
            if self.rank == 1:
                return False
            elif other.rank == 1:
                return True
            else:
                return self.rank < other.rank
        return aSuit < bSuit

class BridgeHand:
    def __init__(self, hand):
        self.hand = hand

    def countPoints(self):
        # Distribution points
        # Total Points
        totalPoints = highCardPoints + distributionPoints
        return totalPoints
    
    def highCardPoints(self):
        points = 0
        for card in self.hand:
            if card.rank == 1:
                points = points + 4
            elif card.rank > 10:
                points = points + (card.rank - 10)
        return points
    
    def suitLengths(self):
        lengths = [0, 0, 0, 0]
        for card in self.hand:
            i = SUITS.index(card.suit)
            lengths[i] = lengths[i] + 1
        return lengths
    
    def longSuitPoints(self):
        points = 0
        for l in self.suitLengths():
            if l > 4:
                points = points + (l - 4)
        return points

    def openingBid(self):
        # No Trump Bids
        hcp = self.highCardPoints()
        if 20 <= hcp <= 21:
            return "2NT"
        elif 15 <= hcp <= 17:
            return "1NT"
        # Suit Bids
        lengths = self.suitLengths()
        lsp = self.longSuitPoints()
        tp = hcp + lsp
        if 13 <= tp <= 21:
            if lengths[0] >= 5 or lengths[1] >= 5:
                # Major
                if lengths[0] >= lengths[1]:
                    return "1S"
                else:
                    return "1H"
            elif lengths[2] >= 3 or lengths[3] >= 3:
                if lengths[2] >= lengths[3]:
                    return "1D"
                else:
                    return "1C"
        elif tp >= 22:
            return "2C"
        elif 5 <= hcp <= 10:
            if lengths[0] >= 6:
                return "2S"
            elif lengths[1] >= 6:
                return "2H"
            elif lengths[2] >= 6:
                return "2D"
        # Default
        return "PASS"

class BridgeApp:
    def __init__(self):
        pass

    def run(self):
        deck = self.newShuffledDeck()
        hands = [[], [], [], []]
        for i in range(len(deck)):
            hands[i%4].append(deck[i])
        bridgeHands = []
        for h in hands:
            h.sort(reverse=True)
            bridgeHands.append(BridgeHand(h))
        for bh in bridgeHands:
            print(f'{bh.openingBid():>4} - {bh.hand}')

    def newShuffledDeck(self):
        deck = []
        for suit in SUITS:
            for rank in RANKS:
                deck.append(Card(suit, rank))
        random.shuffle(deck)
        return deck

def main():
    app = BridgeApp()
    app.run()

main()