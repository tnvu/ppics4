# The days of the year are often numbered from 1 through 365 (or 366).
# This number can be computed in three steps using int arithmetic:
#       (a) dayNum = 31(month — 1) + day
#       (b) if the month is after February subtract (4(month) + 23)//10
#       (c) if it’s a leap year and after February 29, add 1
# Write a program that accepts a date as month/day/year, verifies that it is a
# valid date (see previous problem), and then calculates the corresponding
# day number.

### COPIED FROM EXERCISE-11 ###
def isLeapYear(year):
    leap_year = False
    if year % 4 == 0:
        # Leap year if divisible by 4
        leap_year = True
        if year % 100 == 0 and year % 400 != 0:
            # Unless it is a century year that is not divisible by 400
            leap_year = False
    return leap_year

### COPIED FROM EXERCISE-12 ###
def isValidDate(month, day, year):
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
    return valid_date

def main():
    month = int(input("Month: "))
    day = int(input("Day: "))
    year = int(input("Year: "))

    if not isValidDate(month, day, year):
        print("Invalid date: month=", month, "day=", day, "year=", year)
    else:
        dayNum = 31 * (month - 1) + day
        if month > 2:
            dayNum = dayNum - (4 * month + 23)//10
        if isLeapYear(year) and month > 2:
            dayNum = dayNum + 1
        print("Day of the year: ", dayNum)

main()