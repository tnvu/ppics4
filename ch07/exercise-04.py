# Modify the previous program to find every prime number less than or equal
# to n.

import math

### COPIED FROM CH07 EXERCISE 03 ###
def is_prime(n):
    x = 2
    while x <= math.sqrt(n):
        if n % x == 0:
            return False
        x = x + 1
    return True

def main():
    n = int(input("Enter a number >= 2: "))
    for i in range(2, n+1):
        if is_prime(i):
            print(i)

main()