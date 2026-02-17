# Suppose you are doing a random walk (see previous problem) on the blocks of
# a city street. At each “step” you choose to walk one block (at random) 
# either forward, backward, left or right. In n steps, how far do you expect
# to be from your starting point? Write a program to help answer this
# question.

import math
import random

def main():
    n = int(input("Number of steps: "))
    x = y = 0
    for _ in range(n):
        s = random.randint(0, 3)
        if s == 0:
            x = x + 1
        elif s == 1:
            x = x - 1
        elif s == 2:
            y = y + 1
        else:
            y = y - 1
    print(f"Distance = {math.sqrt(x**2 + y**2)}")

main()