# A certain CS professor gives 100-point exams that are graded on the scale
# 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts
# an exam score as input and prints out the corresponding grade. Use a 
# string lookup table instead of a decision.

def main():
    GRADES = 'FFFFFFDCBAA'

    score = int(input("Enter exam score: "))
    print("Grade =", GRADES[score//10])

main()
