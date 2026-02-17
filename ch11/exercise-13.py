# Write a program that performs a simulation to estimate the probability of
# rolling five of a kind in a single roll of five six-sided dice.

import random

def main():
    n = int(input("How many simulations? "))
    fiveMatches = 0
    for _ in range(n):
        r0 = random.randint(1, 6)
        match = True
        for _ in range(4):
            if r0 != random.randint(1, 6):
                match = False
                break
        if match:
            fiveMatches = fiveMatches + 1
    print(f"Five matches: {fiveMatches} out of {n} ({fiveMatches/n:0.3%})")

main()