# The Goldbach conjecture asserts that every even number is the sum of two
# prime numbers. Write a program that gets a number from the user, checks
# to make sure that it is even, and then finds two prime numbers that add
# up to the number.

import math

def is_even(n):
    return n % 2 == 0

def is_prime(n):
    x = 2
    while x <= math.sqrt(n):
        if n % x == 0:
            return False
        x = x + 1
    return True

def main():
    n = -1
    while not is_even(n):
        n = int(input("Please enter an even number > 2: "))
    primes_found = False
    for a in range(2, n):
        b = n - a
        if is_prime(a) and is_prime(b):
            primes_found = True
            print("Prime numbers are:", a, "and", b)
            break
    if not primes_found:
        print("No primes found:", n)

main()