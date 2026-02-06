# The greatest common divisor (GCD) of two values can be computed using
# Euclid’s algorithm. Starting with the values m and n, we repeatedly apply
# the formula: n, m = m, n%m until m is 0. At that point, n is the GCD of
# the original m and n. Write a program that finds the GCD of two numbers
# using this algorithm.

def gcd(m, n):
    while m != 0:
        n, m = m, n%m
    return n

def main():
    m = int(input("Enter first number: "))
    n = int(input("Enter second number: "))
    x = gcd(m, n)
    print("GCD =", x)

main()