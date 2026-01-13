# The Gregorian epact is the number of days between January 1st and the
# previous new moon. This value is used to figure out the date of Easter. It
# is calculated by these formulas (using int arithmetic):
#       C = year / 100
#       epact =  (8 + (C//4) - C + ((8C + 13)//25) + 11(year%19)) % 30
# Write a program that prompts the user for a four-digit year and then outputs
# the value of the epact.

def main():
    year = int(input("Enter four-digit year: "))
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
    print("Epact = ", epact)

main()