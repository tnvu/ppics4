# A certain CS professor gives 5-point quizzes that are graded on the scale
# 5-A, 4-B, 3-C, 2-D, 1-F, O-F. Write a program that accepts a quiz score as
# an input and prints out the corresponding grade. Use a string as a lookup
# table instead of a decision.

def main():
    GRADES = 'FFDCBA'

    score = int(input("Enter quiz score: "))
    print("Grade =", GRADES[score])

main()