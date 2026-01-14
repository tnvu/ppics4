# Write a program to find the sum of the cubes of the first n natural numbers
# where the value of n is provided by the user.

def main():
    n = int(input("Enter n: "))
    sum = 0
    for i in range(n+1):
        sum = sum + i**3
    print("Sum = ", sum)

main()