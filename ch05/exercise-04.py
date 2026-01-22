# Write definitions for the following two functions:
#   sumN(n) returns the sum of the first n natural numbers.
#   sumNCubes (n) returns the sum of the cubes of the first n natural numbers.
# Then use these functions in a program that prompts a user for an n and
# prints out the sum of the first n natural numbers and the sum of the cubes
# of the first n natural numbers.

def sumN(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

def sumNCubes(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i**3)
    return sum

def main():
    n = int(input("Enter n: "))
    print("Sum of first n natural numbers: ", sumN(n))
    print("Sum of cubes of first n natural numbers: ", sumNCubes(n))

main()