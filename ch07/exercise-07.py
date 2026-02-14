# Write a program that computes the fuel efficiency of a multi-leg journey.
# The program will first prompt for the starting odometer reading and then
# get information about a series of legs. For each leg, the user enters the
# current odometer reading and the amount of gas used. The user signals
# the end of the trip with a blank line. The program should print out the
# miles per gallon achieved on each leg and the total MPG for the trip.

def main():
    odo_start = float(input("Enter starting odometer: "))
    total_mileage = 0.0
    total_gas_used = 0.0
    while True:
        odo_current = input("Enter current odometer: ")
        if odo_current == "": break
        odo_current = float(odo_current)
        mileage = odo_current - (odo_start + total_mileage)

        gas_used = input("Enter amount of gas used: ")
        if gas_used == "": break
        gas_used = float(gas_used)
        
        print("Leg mpg =", mileage / gas_used)
        total_mileage = total_mileage + mileage
        total_gas_used = total_gas_used + gas_used
    print("Overall mpg =", total_mileage / total_gas_used)

main()