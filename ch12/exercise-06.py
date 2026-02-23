# Extend the previous exercise by implementing an addLetterGrade method.
# This is similar to addGrade except that it accepts a letter grade as a 
# string (instead of gradePoint). Use the updated class to improve the GPA
# calculator by allowing the entry of letter grades.

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

    def addGrade(self, gradePoint, credits):
        g = float(gradePoint)
        c = float(credits)
        self.qpoints = self.qpoints + (g * c)
        self.hours = self.hours + c

    def addLetterGrade(self, letterGrade, credits):
        if letterGrade == "A":    self.addGrade(4.0, credits)
        elif letterGrade == "A-": self.addGrade(3.7, credits)
        elif letterGrade == "B+": self.addGrade(3.3, credits)
        elif letterGrade == "B":  self.addGrade(3.0, credits)
        elif letterGrade == "B-": self.addGrade(2.7, credits)
        elif letterGrade == "C+": self.addGrade(2.3, credits)
        elif letterGrade == "C":  self.addGrade(2.0, credits)
        elif letterGrade == "C-": self.addGrade(1.7, credits)
        elif letterGrade == "D+": self.addGrade(1.3, credits)
        elif letterGrade == "D":  self.addGrade(1.0, credits)
        elif letterGrade == "D-": self.addGrade(0.7, credits)
        elif letterGrade == "F+": self.addGrade(0.3, credits)
        elif letterGrade == "F":  self.addGrade(0.0, credits)
        else: raise ValueError("Unknown grade: ", letterGrade)

def main():
    student = Student("", 0, 0)
    while True:
        s = input("Enter the grade and credits separated by whitespace. " + \
                  "<Return> to quit: ")
        if s == "":
            break
        grade, credits = s.split(maxsplit=2)
        if grade[0] in ('A', 'B', 'C', 'D', 'F'):
            student.addLetterGrade(grade, credits)
        else:
            student.addGrade(grade, credits)
    print(f"GPA = {student.gpa():0.2f}")

main()