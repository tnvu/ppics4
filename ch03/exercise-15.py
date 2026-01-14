# Write a program that approximates the value of pi by summing the terms
# of this series: 4/1 — 4/3 + 4/5 — 4/7 + 4/9 — 4/11 + ... The program should
# prompt the user for n, the number of terms to sum, and then output the
# sum of the first n terms of this series. Have your program subtract the
# approximation from the value of math.pi to see how accurate it is.

import math

def main():
    n = int(input("Number of terms to sum: "))
    sum = 0
    sign = 1
    for i in range(n):
        term = 4 / (2 * i + 1)
        sum = sum + sign * term
        sign = sign * -1
    diff = sum - math.pi
    print("Sum = ", sum, ", diff = ", diff)

main()