# Take a favorite programming problem from a previous chapter and add
# decisions and/or exception handling as required to make it truly robust
# (will not crash on any inputs). Trade your program with a friend and have
# a contest to see who can “break” the other’s program.

### COPIED FROM CH05 EXERCISE 08 ###
import math

def nextGuess(guess, x):
    g = (guess + (x / guess)) / 2
    return g

def main():
    try:
        x = float(input("Enter x: "))
        n = int(input("Number of times to improve guess: "))
        guess = x / 2.0
        for _ in range(n):
            guess = nextGuess(guess, x)
            diff = guess - math.sqrt(x)
        print("Guess = ", guess, ", Diff = ", diff)
    except ValueError:
        print("Please ensure x is a float and number of times to improve"
              + "guesses is an integer")

main()