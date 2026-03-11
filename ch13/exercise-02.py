# Using the ideas from this chapter, implement a simulation of another racquet
# game. See the programming exercises from Chapter 11 for some ideas.

import random

def getInputs():
    sideoutA = float(input("What is the sideout % of team A? "))
    sideoutB = float(input("What is the sideout % of team B? "))
    nGames = int(input("How many games to simulate? "))
    return (sideoutA, sideoutB, nGames)

class VolleyballStats:
    def __init__(self):
        self.winsA = 0
        self.winsB = 0

    def update(self, scoreA, scoreB):
        if scoreA > scoreB:
            self.winsA = self.winsA + 1
        else:
            self.winsB = self.winsB + 1

class Team:
    def __init__(self, sideout):
        self.sideout = sideout

class VolleyballGame:
    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB

    def play(self):
        scoreA = 0
        scoreB = 0
        server = random.choice([self.teamA, self.teamB])
        while not self.gameOver(scoreA, scoreB):
            if server == self.teamA:
                if random.random() < self.teamB.sideout:
                    server = self.teamB
                    scoreB = scoreB + 1
                else:
                    scoreA = scoreA + 1
            else:
                if random.random() < self.teamA.sideout:
                    server = self.teamA
                    scoreA = scoreA + 1
                else:
                    scoreB = scoreB + 1
        return scoreA, scoreB
    
    def gameOver(self, scoreA, scoreB):
        return (scoreA >= 21 or scoreB >= 21) and \
            (abs(scoreA - scoreB) >= 2)

def main():
    sideoutA, sideoutB, nGames = getInputs()
    stats = VolleyballStats()
    for _ in range(nGames):
        teamA = Team(sideoutA)
        teamB = Team(sideoutB)
        game = VolleyballGame(teamA, teamB)
        scoreA, scoreB = game.play()
        stats.update(scoreA, scoreB)
    print(f"TeamA wins = {stats.winsA}, TeamB wins = {stats.winsB}")

main()