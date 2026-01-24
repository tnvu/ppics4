# A babysitter charges $12.50 an hour until 9:00 PM when the rate drops to
# $11.50 an hour (the children are in bed). Write a program that accepts a
# starting time and ending time in hours and minutes and calculates the total
# babysitting bill. You may assume that the starting and ending times are in
# a single 24-hour period. Partial hours should be appropriately prorated.

def main():
    # 9PM in minutes since start of day
    time_2100 = 21 * 60

    time_start = int(input("Starting hour (0-23): ")) * 60
    time_start = time_start + int(input("Starting minute (0-59): "))
    time_end = int(input("Ending hour (0-23): ")) * 60
    time_end = time_end + int(input("Ending minute (0-59): "))

    if time_end < time_2100:
        # End before 9PM
        bill = (time_end - time_start) / 60 * 12.50
    else:
        # End after 9PM - calculate up to 9PM and then after
        bill = (time_2100 - time_start) / 60 * 12.50
        bill = bill + (time_end - time_2100) / 60 * 11.50

    print("Bill = ", bill)

main()