# Design and implement a simulation of the game of volleyball. Some 
# recreational volleyball leagues use side out scoring, which is like
# racquetball in that a team can only score points when it is serving. Games 
# are played to 15, but must be won by at least two points.

from random import random


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def printIntro():
    print("This program simulates a game of volleyball between two")
    print('teams called "A" and "B".  The abilities of each team is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point when serving.\n")


def getInputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. team A wins a serve? "))
    b = float(input("What is the prob. team B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def simNGames(n, probA, probB):
    # Simulates n games of volleyball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        firstServer = 'A'
        if i % 2 == 0: firstServer = 'B'
        scoreA, scoreB = simOneGame(probA, probB, firstServer)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB, firstServer):
    # Simulates a single game or racquetball between players whose
    #    abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = firstServer
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
    print(f'scoreA={scoreA}, scoreB={scoreB}')
    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return (a >= 15 or b >= 15) and abs(a - b) >= 2


def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print(f"Wins for A: {winsA} ({winsA/n:0.1%})")
    print(f"Wins for B: {winsB} ({winsB/n:0.1%})")


if __name__ == '__main__':
    main()