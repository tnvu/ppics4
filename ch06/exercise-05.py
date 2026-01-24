# The body mass index (BMI) is calculated as a person’s weight (in pounds)
# times 703, divided by the square of the person’s height (in inches). A BMI
# in the range 19-25, inclusive, is considered healthy. Write a program that
# calculates a person’s BMI and prints a message telling whether they are
# above, within, or below the healthy range.

def main():
    weight = float(input("Weight (pounds): "))
    height = float(input("Height (inches): "))
    bmi = (weight * 703) / (height**2)
    if bmi < 19:
        bmi_range = 'below healthy range'
    elif 19 <= bmi <= 25:
        bmi_range = 'within healthy range'
    elif bmi > 25:
        bmi_range = 'above healthy range'
    print("BMI range = ", bmi_range)

main()