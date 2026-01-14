# You have seen that the math library contains a function that computes
# the square root of numbers. In this exercise, you are to write your own
# algorithm for computing square roots. One way to solve this problem
# is to use a guess-and-check approach. You first guess what the square
# root might be, and then see how close your guess is. You can use this
# information to make another guess and continue guessing until you have
# found the square root (or a close approximation to it). One particularly
# good way of making guesses is to use Newton’s method. Suppose x is the
# number we want the root of, and guess is the current guessed answer. The
# guess can be improved by computing the next guess as:
#       guess + x / guess
#       -----------------
#               2
# Write a program that implements Newton’s method. The program
# should prompt the user for the value to find the square root of (x) and
# the number of times to improve the guess. Starting with a guess value
# of x/2, your program should loop the specified number of times applying
# Newton’s method and report the final value of guess. You should also
# subtract your estimate from the value of math.sqrt(x) to show how close
# it is.

import math

def main():
    x = float(input("Enter x: "))
    n = int(input("Number of times to improve guess: "))
    guess = x / 2.0
    for _ in range(n):
        guess = (guess + (x / guess)) / 2
    diff = guess - math.sqrt(x)
    print("Guess = ", guess, ", Diff = ", diff)

main()