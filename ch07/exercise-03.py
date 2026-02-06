# A positive whole number n > 2 is prime if no number between 2 and sqrt(n)
# (inclusive) evenly divides n. Write a program that accepts a value of n as
# input and determines if the value is prime. If n is not prime, your program
# should quit as soon as it finds a value that evenly divides n.

import math

def main():
    n = int(input("Enter n (>2): "))
    x = 2
    is_prime = True
    while x <= math.sqrt(n):
        if n % x == 0:
            is_prime = False
            break
        x = x + 1
    if is_prime:
        print("Is prime: ", n)
    else:
        print("Is not prime: ", n)

main()