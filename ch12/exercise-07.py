# Passing a function to the list sort method makes the sorting slower, since
# this function is called repeatedly as Python compares various list items.
# An alternative to passing a key function is to create a “decorated” list
# that will sort in the desired order using the standard Python ordering. For
# example, to sort Student objects by GPA, we could first create a list of
# tuples [(gpa0, Student0), (gpal, Student1), ..] and then sort this
# list without passing a key function. These tuples will get sorted into GPA
# order. The resulting list can then be traversed to rebuild a list of student
# objects in GPA order. Redo the gpasort program using this approach.

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
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    data = [(s.gpa(), i, s) for i, s in enumerate(data)]
    data.sort(reverse=True)
    data = [s for gpa, i, s in data]
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()