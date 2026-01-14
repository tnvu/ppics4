# Write a program to sum a series of numbers entered by the user. The
# program should first prompt the user for how many numbers are to be
# summed. The program should then prompt the user for each of the numbers
# in turn and print out a total sum after all the numbers have been
# entered. Hint: Use an input statement in the body of the loop.

def main():
    n = int(input("How many numbers to be summed: "))
    sum = 0
    for _ in range(n):
        x = float(input("Enter number: "))
        sum = sum + x
    print("Sum = ", sum)

main()