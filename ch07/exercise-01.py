# Write a program that uses a while loop to determine how long it takes
# for an investment to double at a given interest rate. The input will be an
# annualized interest rate, and the output is the number of years it takes an
# investment to double. Note: The amount of the initial investment does not
# matter; you can use $1.

def main():
    r = float(input("Annualized interest rate: "))
    p = 1
    y = 0
    while p < 2:
        p = p * (1 + r)
        y = y + 1
    print("Number of years = ", y)

main()
