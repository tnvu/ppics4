# Suppose you have an investment plan where you invest a certain fixed amount
# every year. Modify futval.py (Section 2.7) to compute the total accumulation
# of your investment. The inputs to the program will be the amount to invest
# each year, the interest rate, and the number of years for the investment.

def main():
    print("This program calculates the future value")
    
    investment = float(input("Enter the yearly investment: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))

    principal = 0
    for _ in range(years):
        principal = (principal + investment) * (1 + apr)

    print("The value in", years, "years is:", principal)

main()