# Extend the gpasort program so that it allows the user to sort a file of
# students based on GPA, name, or credits. Your program should prompt for
# the input file, the field to sort on, and the output file.

# gpa1.py
#    Program to find student with highest GPA

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


def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

# gpasort.py
#    A program to sort student information into GPA order.


def readStudents(filename):
    with open(filename, 'r') as infile:
        students = [makeStudent(line) for line in infile]
    return students


def writeStudents(students, filename):
    # students is a list of Student objects
    with open(filename, 'w') as outfile:
        for s in students:
            print(f"{s.getName()}\t{s.getHours()}\t{s.getQPoints()}",
                  file=outfile)
            
def main():
    print("This program sorts student grade information")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    while True:
        field = int(input("Field to sort: 1 = GPA, 2 = Name, 3 = Credits: "))
        if field == 1:
            data = [(s.gpa(), i, s) for i, s in enumerate(data)]
            break
        elif field == 2:
            data = [(s.getName(), i, s) for i, s in enumerate(data)]
            break
        elif field == 3:
            data = [(s.getHours(), i, s) for i, s in enumerate(data)]
            break
        else:
            print("Try again.")
    data.sort()
    data = [s for gpa, i, s in data]
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()