# Craps is a dice game played at many casinos. A player rolls a pair of normal
# six-sided dice. If the initial roll is 2, 3, or 12, the player loses. If the
# roll is 7 or 11, the player wins. Any other initial roll causes the player
# to “roll for point.” That is, the player keeps rolling the dice until either
# rolling a 7 or re-rolling the value of the initial roll. If the player 
# re-rolls the initial value before rolling a 7, it’s a win. Rolling a 7 first
# is a loss. Write a program to simulate multiple games of craps and estimate
# the probability that the player wins. For example, if the player wins 249
# out of 500 games, then the estimated probability of winning 
# is 249/500 = 0.498.

import random

def rollDice():
    return random.randint(1, 6) + random.randint(1, 6)

def simulateOneGame():
    roll = rollDice()
    if roll in (2, 3, 12):
        return False
    if roll in (7, 11):
        return True
    
    point = roll
    while True:
        roll = rollDice()
        if roll == point:
            return True
        elif roll == 7:
            return False

def main():
    n = int(input("Number of gmaes: "))
    wins = 0
    for _ in range(n):
        if simulateOneGame():
            wins = wins + 1
    print(f'Number of wins {wins}/{n} ({wins/n:0.2%})')
    
main()