# The formula for Easter in the previous problem works for every year in
# the range 1900-2099 except for 1954, 1981, 2049, and 2076. For these
# four years it produces a date that is one week too late. Modify the above
# program to work for the entire range 1900-2099.

def main():
    year = int(input("Year: "))
    if year < 1900 or year > 2099:
        print("Invalid year: ", year)
    else:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        day = 22 + d + e
        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            # One week earlier
            day = day - 7
        
        # March has 31 days
        if day <= 31:
            month = 'March'
        else:
            month = 'April'
            day = day - 31
        print("Easter = ", month, day)

main()