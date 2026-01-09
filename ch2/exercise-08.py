# As an alternative to APR, the interest accrued on an account is often
# described in terms of a nominal rate and the number of compounding periods.
# For example, if the interest rate is 3% and the interest is compounded 
# quarterly, the account actually earns 3/4% interest every three months.
# Modify the futval.py program to use this method of entering the interest
# rate. The program should prompt the user for the nominal rate (rate) and the
# number of times that the interest is compounded each year (periods, an int).
# To compute the value in ten years, the program will loop 10 * periods times
# and accrue rate/period interest on each iteration.

def main():
    print("This program calculates the future value")
    
    principal = float(input("Enter the initial investment: "))
    apr = float(input("Enter the nominal interest rate: "))
    periods = int(input("Number of compounding periods: "))
    
    for _ in range(10 * periods):
        principal = principal * (1 + (apr / periods))

    print("The value in 10 years is:", principal)

main()