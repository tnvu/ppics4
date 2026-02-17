# A random walk is a particular kind of probabilistic simulation that models
# certain statistical systems such as the Brownian motion of molecules. You
# can think of a one-dimensional random walk in terms of coin flipping.
# Suppose you are standing on a very long straight sidewalk that extends
# both in front of and behind you. You flip a coin. If it comes up heads, you
# take a step forward; tails means to take a step backward.
# Suppose you take a random walk of n steps. On average, how many
# steps away from the starting point will you end up? Write a program to
# help you investigate this question.

import random

def oneTrial(nSteps):
    s = 0
    for _ in range(nSteps):
        if random.random() < 0.50:
            s = s + 1
        else:
            s = s - 1
    return s

def nTrials(nTrials, nSteps):
    data = []
    for _ in range(nTrials):
        data.append(oneTrial(nSteps))
    return data

def main():
    numTrials = int(input("Number of trials: "))
    numSteps = [1, 10, 100, 1000 , 10000]
    avgSteps = []
    for nSteps in numSteps:
        data = nTrials(numTrials, nSteps)
        avgSteps.append(sum(data)/numTrials)
    for i in range(len(numSteps)):
        print(f'{numSteps[i]} = {avgSteps[i]}')
    

main()