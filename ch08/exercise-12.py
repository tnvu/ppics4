# The National Weather Service computes the windchill index using the 
# following formula:
#           35.74 + 0.6215T — 35.75(V^0.16) + 0.4275T(V^0.16)
# Where T is the temperature in degrees Fahrenheit, and V is the wind speed
# in miles per hour.
# Write a program that prints a nicely formatted table of windchill values.
# Rows should represent wind speed for 0 to 50 in 5-mph increments,
# and the columns represent temperatures from —20 to +60 in 10-degree
# increments. Note: The formula only applies for wind speeds in excess of
# three miles per hour.

def windchill_index(t, v):
    return 35.74 + 0.6215 * t - 35.75 * v**0.16 + 0.4275 * t * v**0.16

def main():
    # print temperature header
    print("|  v\\t |", end='')
    for t in range(-20, 70, 10):
        print(f" {t:^6} |", end='')
    print()

    for v in range(5, 55, 5):
        print(f"| {v:4} |", end="")
        for t in range(-20, 70, 10):
            print(f" {windchill_index(t, v):6.2f} |", end="")
        print()

main()