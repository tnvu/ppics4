# Modify the previous program to keep a visit histogram. Consider the sidewalk
# as a sequence of squares, and each step moves the walker one square forward
# or back. Your program should keep track of how many times each square of the
# sidewalk is stepped on. Start your walker in the middle of a sidewalk of 
# length n where n is a user input, and continue the simulation until it drops
# off one of the ends. Then print out the counts of how many times each square
# was landed on.

import random

def main():
    n = int(input("Number of steps: "))
    steps = [0] * n
    pos = n // 2
    while True:
        if random.random() < 0.50:
            pos = pos + 1
        else:
            pos = pos - 1
        print(f'pos={pos}')
        if 0 <= pos < n:
            steps[pos] = steps[pos] + 1
        else:
            # Drop off one of the ends
            break
    for i in range(n):
        print(f'{i} = {steps[i]}')

main()
