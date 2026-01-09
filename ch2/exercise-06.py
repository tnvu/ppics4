# Modify the futval.py program (Section 2.7) so that the number of years for
# the investment is also a user input (Note: This will be an int value). Make
# sure to change the final message to reflect the correct number of years.

def main():
    print("This program calculates the future value")
    
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))

    for _ in range(years):
        principal = principal * (1 + apr)
    
    print("The value in", years, "years is:", principal)

main()