# Write a program that finds the average of a series of numbers entered by
# the user. As in the previous problem, the program will first ask the user
# how many numbers there are.

def main():
    n = int(input("How many numbers: "))
    sum = 0
    for _ in range(n):
        x = float(input("Enter number: "))
        sum = sum + x
    average = sum / n
    print("Average = ", average)

main()