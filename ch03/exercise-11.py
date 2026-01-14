# Write a program to find the sum of the first » natural numbers, where the
# value of n is provided by the user.

def main():
    n = int(input("Enter n: "))
    sum = 0
    for i in range(n+1):
        sum = sum + i
    print("Sum = ", sum)

main()