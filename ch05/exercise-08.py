# Solve Programming Exercise 17 from Chapter 3 using a function
# nextGuess(guess, x) that returns the next guess.

import math

def nextGuess(guess, x):
    g = (guess + (x / guess)) / 2
    return g

def main():
    x = float(input("Enter x: "))
    n = int(input("Number of times to improve guess: "))
    guess = x / 2.0
    for _ in range(n):
        guess = nextGuess(guess, x)
    diff = guess - math.sqrt(x)
    print("Guess = ", guess, ", Diff = ", diff)

main()