# Blackjack (Twenty-One) is a casino game played with cards. The goal
# of the game is to draw cards that total as close to 21 points as possible
# without going over. All face cards count as 10 points, aces count as 1 or
# 11, and all other cards count their numeric value.
# The game is played against a dealer. The player tries to get closer to
# 21 (without going over) than the dealer. If the dealer busts (goes over
# 21), the player automatically wins (provided the player had not already
# busted). The dealer must always take cards according to a fixed set of
# rules. The dealer takes cards until he or she achieves a total of at least
# 17. If the dealer’s hand contains an ace, it will be counted as 11 when
# that results in a total between 17 and 21 inclusive; otherwise, the ace is
# counted as 1.
# Write a program that simulates multiple games of blackjack and estimates the
# probability that the dealer will bust. Hints: Treat the deck of cards as
# infinite (casinos use a “shoe” containing many decks). You do not need to
# keep track of the cards in the hand, just the total so far (treating an ace
# as 1) and a bool variable hasAce that tells whether or not the hand contains
# an ace. A hand containing an ace should have 10 points added to the total
# exactly when doing so would produce a stopping total (something between 17
# and 21 inclusive).

import random

def initializeDeck():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['C', 'D', 'H', 'S']
    deck = []
    for r in ranks:
        for s in suits:
            c = (r, s)
            deck.append(c)
    return deck


def washDeck(deck):
    for _ in range(len(deck)):
        i = random.randint(0, len(deck)-1)
        j = random.randint(0, len(deck)-1)
        deck[i], deck[j] = deck[j], deck[i]


def riffleDeck(deck):
    split = len(deck) // 2
    for i in range(split):
        c = deck.pop(split+i)
        deck.insert(2 * i + 1, c)


def boxDeck(deck):
    split = random.randint(0, len(deck)-1)
    for i in range(split):
        c = deck.pop(0)
        deck.append(c)


def shuffleDeck(deck):
    washDeck(deck)
    riffleDeck(deck)
    riffleDeck(deck)
    boxDeck(deck)
    riffleDeck(deck)

def drawCard(deck):
    return deck.pop(0)

def playDealerHand(deck):
    cards = []
    totals = [0]
    while True:
        c = drawCard(deck)
        cards.append(c)
        if c[0] == 'A':
            plus_eleven = []
            for i in range(len(totals)):
                plus_eleven.append(totals[i] + 11)
                totals[i] = totals[i] + 1
            totals.extend(plus_eleven)
        elif c[0] in ('J', 'Q', 'K'):
            for i in range(len(totals)):
                totals[i] = totals[i] + 10
        else:
            for i in range(len(totals)):
                totals[i] = totals[i] + c[0]

        all_over_21 = True
        for t in totals:
            if t <= 21:
                all_over_21 = False
            if 17 <= t <= 21:
                return t
        if all_over_21:
            return 22

def main():
    n = int(input("Number of games: "))
    busted = 0
    for _ in range(n):
        deck = initializeDeck()
        shuffleDeck(deck)
        value = playDealerHand(deck)
        if value > 21:
            busted = busted + 1
    print(f"Number of games busted {busted} ({busted/n:0.2%}) out of {n}")

main()