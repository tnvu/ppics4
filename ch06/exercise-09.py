# A formula for computing Easter in the years 1982-2048, inclusive, is as
# follows: let a = year%19, b = year%4, c = year%7, d = (19a + 24)%30,
# e = (2b + 4c + 6d + 5)%7. The date of Easter is March 22 + d + e (which
# could be in April). Write a program that inputs a year, verifies that it is
# in the proper range, and then prints out the date of Easter that year.

def main():
    year = int(input("Year: "))
    if year < 1982 or 2048 < year:
        print("Invalid year: ", year)
    else:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        
        # March has 31 days
        if (22 + d + e) <= 31:
            month = 'March'
            day = 22 + d + e
        else:
            month = 'April'
            day = (22 + d + e) - 31
        print("Easter = ", month, day)

main()