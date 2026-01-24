# The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph
# over the limit plus a penalty of $200 for any speed over 90 mph. Write a
# program that accepts a speed limit and a clocked speed and either prints
# a message indicating the speed was legal or prints the amount of the fine,
# if the speed is illegal.

def main():
    speed_limit = float(input("Speed limit: "))
    clocked_speed = float(input("Clocked speed: "))
    fine = 0
    if clocked_speed > speed_limit:
        fine = 50 + 5 * (clocked_speed - speed_limit)
        if clocked_speed > 90:
            fine = fine + 200
    if fine == 0:
        print("Speed was legal.")
    else:
        print("Fine = ", fine)

main()