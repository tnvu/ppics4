# A certain college classifies students according to credits earned. A student
# with less than 7 credits is a Freshman. At least 7 credits are required to be
# a Sophomore, 16 to be a Junior and 26 to be classified as a Senior. Write a
# program that calculates class standing from the number of credits earned.

def main():
    credits = int(input("Number of credits: "))
    if credits < 7:
        student = 'Freshman'
    elif credits < 16:
        student = 'Sophomore'
    elif credits < 26:
        student = 'Junior'
    else:
        student = 'Senior'
    print("Student = ", student)

main()