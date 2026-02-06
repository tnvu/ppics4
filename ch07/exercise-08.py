# Heating and cooling degree days are measures used by utility companies
# to estimate energy requirements. If the average temperature for a day is
# below 60, then the number of degrees below 60 is added to the heating
# degree days. If the temperature is above 80, the amount over 80 is added
# to the cooling degree days. Write a program that accepts a sequence of
# average daily temperatures and computes the running total of cooling and
# heating degree days. The program should print these two totals after all
# the data has been processed.

def main():
    heating_days = 0
    cooling_days = 0

    while True:
        t = input("Enter the average temperate (blank to stop): ")
        if t == "": break
        t = float(t)
        if t < 60:
            heating_days = heating_days + (60 - t)
        elif t > 80:
            cooling_days = cooling_days + (t - 80)

    print("Number of heating days: " + str(heating_days) + 
          ", number of cooling days: " + str(cooling_days))

main()