# A blackjack dealer always starts with one card showing. It would be useful
# for a player to know the dealer’s bust probability (see previous problem)
# for each possible starting value. Write a simulation program that runs
# multiple hands of blackjack for each possible starting value (ace-10) and
# estimates the probability that the dealer busts for each starting value.

import random

def initializeDeck():
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
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
                return cards, t
        if all_over_21:
            return cards, 22

def main():
    n = int(input("Number of games: "))
    busted = [0] * 10
    for _ in range(n):
        deck = initializeDeck()
        shuffleDeck(deck)
        cards, value = playDealerHand(deck)
        if value > 21:
            rank = cards[0][0]
            if rank == 'A':
                busted[0] = busted[0] + 1
            elif rank in ('J', 'Q', 'K'):
                busted[9] = busted[9] + 1
            else:
                busted[rank-1] = busted[rank-1] + 1
    for i in range(len(busted)):
        if i == 0:
            print(' A: ', end='')
        else:
            print(f"{i+1:>2}: ", end='')
        busts = busted[i]
        print(f"{busts:>4} ({busts/n:0.2%})")

main()