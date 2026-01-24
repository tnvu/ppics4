# A year is a leap year if it is divisible by 4, unless it is a century year
# that is not divisible by 400. (1800 and 1900 are not leap years while 1600
# and 2000 are.) Write a program that calculates whether a year is a leap
# year.

def main():
    year = int(input("Year: "))
    leap_year = False
    if year % 4 == 0:
        # Leap year if divisible by 4
        leap_year = True
        if year % 100 == 0 and year % 400 != 0:
            # Unless it is a century year that is not divisible by 400
            leap_year = False
    print("Leap Year = ", leap_year)

main()