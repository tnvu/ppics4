# A person is eligible to be a US senator if they are at least 30 years old
# and have been a US citizen for at least 9 years. To be a US representative
# these numbers are 25 and 7, respectively. Write a program that accepts a
# person’s age and years of citizenship as input and outputs their eligibility
# for the Senate and House.

def main():
    age = int(input("Age: "))
    citizenship = int(input("Years of citizenship: "))

    senate = False
    if age >= 30 and citizenship >= 9:
        senate = True
    house = False
    if age >= 25 and citizenship >= 7:
        house = True
    print("Senate =", senate, "\nHouse =", house)

main()