# Modify the Student class from the chapter by adding a mutator method
# that records a grade for the student. Here is the specification of the new
# method:
#       addGrade(self, gradePoint, credits)
#           gradePoint is a float that represents a grade
#               (e.g., A = 4.0, A- = 3.7, B+ = 3.3, etc.),
#           and credits is a float indicating the number of credit hours for
#               the class.
# Modify the student object by adding this grade information.
# Use the updated class to implement a simple program for calculating GPA.
# Your program should create a new student object that has 0 credits and 0
# quality points (the name is irrelevant). Your program should then prompt
# the user to enter course information (gradePoint and credits) for a series
# of courses, and then print out the final GPA achieved.

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

def main():
    student = Student("", 0, 0)
    while True:
        s = input("Enter grade point and credits separated by whitespace. " + \
                  "<Return> to quit: ")
        if s == "":
            break
        gradePoint, credits = s.split(maxsplit=2)
        student.addGrade(gradePoint, credits)
    print(f"GPA = {student.gpa():0.2f}")

main()