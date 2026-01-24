# Write a program that allows the user to enter the day, month and year
# numbers for a date, and then outputs whether or not the date is valid. For
# example 5/24/1962 is valid, but 9/31/2000 is not. (September has only
# 30 days.)

def isLeapYear(year):
    leap_year = False
    if year % 4 == 0:
        # Leap year if divisible by 4
        leap_year = True
        if year % 100 == 0 and year % 400 != 0:
            # Unless it is a century year that is not divisible by 400
            leap_year = False
    return leap_year

def main():
    month = int(input("Month: "))
    day = int(input("Day: "))
    year = int(input("Year: "))

    valid_date = False
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or \
        month == 10 or month == 12:
        if 1 <= day <= 31:
            valid_date = True
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            valid_date = True
    elif month == 2:
        if 1 <= day <= 28:
            valid_date = True
        elif day == 29 and isLeapYear(year):
            valid_date = True
    print("Valid date: ", valid_date)

main()