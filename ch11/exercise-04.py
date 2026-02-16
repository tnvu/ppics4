# Revise the racquetball simulation to take shutouts (when one player fails
# to score any points) into account. Your updated version should report for
# both players the number of wins, percentage of wins, number of shutouts,
# and percentage of wins that are shutouts.

# rball.py
#    Simulation of a racquetball game

from random import random


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, shutoutsA, shutoutsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, shutoutsA, shutoutsB)


def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")


def getInputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = shutoutsA = shutoutsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
            if scoreB == 0:
                shutoutsA = shutoutsA + 1
        else:
            winsB = winsB + 1
            if scoreA == 0:
                shutoutsB = shutoutsB + 1
    return winsA, winsB, shutoutsA, shutoutsB


def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a == 15 or b == 15


def printSummary(winsA, winsB, shutoutsA, shutoutsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print(f"Wins for A: {winsA} ({winsA/n:0.1%}), shutouts {shutoutsA} ({shutoutsA/n:0.1%})")
    print(f"Wins for B: {winsB} ({winsB/n:0.1%}), shutouts {shutoutsB} ({shutoutsB/n:0.1%})")


if __name__ == '__main__':
    main()