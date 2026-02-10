# Write an improved version of the futval.py program from Chapter 2.
# Your program will prompt the user for the amount of the investment, the
# annualized interest rate, and the number of years of the investment. The
# program will then output a nicely formatted table that tracks the value of
# the investment year by year. Your output might look something like this:
#        Year      Value
#        ------------------
#          0       $2000.00
#          1       $2200.00
#          2       $2420.00
#          3       $2662.00
#          4       $2928.20
#          5       $3221.02
#          6       $3543.12
#          7       $3897.43

def main():
    investment = float(input("Investment amount: "))
    rate = float(input("Annualized interest rate: "))
    years = int(input("Number of years: "))

    print("Year       Value")
    print("------------------")
    value = investment
    for i in range(years+1):
        print(f"{i:3}       ${value:4.2f}")
        value = value * (1 + rate)

main()