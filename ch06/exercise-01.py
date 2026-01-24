# Many companies pay time-and-a-half for any hours worked above 40 in a
# given week. Write a program to input the number of hours worked and
# the hourly rate and calculate the total wages for the week.

def main():
    hours = float(input("Number of hours worked: "))
    rate = float(input("Hourly rate: "))
    wages = hours * rate
    if hours > 40:
        hours = hours - 40
        wages = wages + hours * 0.5 * rate
    print("Wages = ", wages)

main()