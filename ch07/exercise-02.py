# The Syracuse (also called “Collatz” or “Hailstone”) sequence is generated
# by starting with a natural number and repeatedly applying the following
# function until reaching 1:
#           syr(x) = x/2 if x is even
#                    3x + 1 if x is odd
# For example, the Syracuse sequence starting with 5 is: 5,16,8,4,2,1. It is
# an open question in mathematics whether this sequence will always go to
# 1 for every possible starting value.
# Write a program that gets a starting value from the user and then prints
# the Syracuse sequence for that starting value.

def main():
    x = int(input("Input x: "))
    while True:
        print(x, end='')

        if x == 1:
            print()
            break

        if x % 2 == 0:
            x = x // 2
        else:
            x = (3*x) + 1
        print(", ", end='')

main()
