# A Fibonacci sequence is a sequence of numbers where each successive
# number is the sum of the previous two. The classic Fibonacci sequence
# begins: 1, 1, 2, 3, 5, 8, 13, .... Write a program that computes the nth
# Fibonacci number where n is a value input by the user. For example, if
# n = 6, then the result is 8. Hints: Consider this an accumulator loop that
# always tracks the current value and the previous value. Start these both at
# 1 (the first two values of the sequence). Use simultaneous assignment to
# set the next values of these two variables each time around the loop.

def main():
    n = int(input("Which Fibonacci number: "))
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a+b
    print("Fibonacci number: ", a)

main()
