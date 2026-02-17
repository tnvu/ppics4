# Design and implement a system that compares volleyball games using side
# out scoring to those using rally scoring. Your program should be useful in
# investigating whether rally scoring magnifies, reduces, or has no effect on
# the relative advantage enjoyed by the better team.

from random import random


def main():
    probA, probB, n = getInputs()
    winsASideOut, winsBsideOut, winsARally, winsBRally = simNGames(n, probA, probB)
    printSummary(winsASideOut, winsBsideOut, winsARally, winsBRally)


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
    winsASideOut = winsBsideOut = 0
    winsARally = winsBRally = 0
    for i in range(n):
        server = 'A'
        if i % 2 == 0:
            server = 'B'
        scoreA, scoreB = simOneSideOutGame(probA, probB, server)
        if scoreA > scoreB:
            winsASideOut = winsASideOut + 1
        else:
            winsBsideOut = winsBsideOut + 1
        scoreA, scoreB = simOneRallyGame(probA, probB, server)
        if scoreA > scoreB:
            winsARally = winsARally + 1
        else:
            winsBRally = winsBRally + 1

    return winsASideOut, winsBsideOut, winsARally, winsBRally


def simOneSideOutGame(probA, probB, firstServer):
    serving = firstServer
    scoreA = 0
    scoreB = 0
    while not gameOverSideOut(scoreA, scoreB):
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


def gameOverSideOut(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return (a >= 15 or b >= 15) and abs(a - b) >= 2


def simOneRallyGame(probA, probB, firstServer):
    serving = firstServer
    scoreA = 0
    scoreB = 0
    while not gameOverRally(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
                serving = "A"
    return scoreA, scoreB


def gameOverRally(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return (a >= 25 or b >= 25) and abs(a - b) >= 2


def printSummary(winsASideOut, winsBsideOut, winsARally, winsBRally):
    # Prints a summary of wins for each player.
    n = winsASideOut + winsBsideOut
    print("\nGames simulated:", n)
    print(f"Sideout wins for A: {winsASideOut} ({winsASideOut/n:0.1%})")
    print(f"Sideout wins for B: {winsBsideOut} ({winsBsideOut/n:0.1%})")
    print(f"Rally wins for A: {winsARally} ({winsARally/n:0.1%})")
    print(f"Rally wins for B: {winsBRally} ({winsBRally/n:0.1%})")


if __name__ == '__main__':
    main()