# A certain CS professor gives 100-point exams that are graded on the scale
# 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts
# an exam score as input and uses a decision structure to calculate the
# corresponding grade.

def main():
    score = int(input("Score: "))
    if score > 100:
        print("Unknown score: ", score)
    else:
        if 90 <= score <= 100:
            grade = 'A'
        elif 80 <= score <= 89:
            grade = 'B'
        elif 70 <= score <= 79:
            grade = 'C'
        elif 60 <= score <= 69:
            grade = 'D'
        elif score < 60:
            grade = 'F'
        print("Grade = ", grade)

main()
