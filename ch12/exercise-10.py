# Give the program from the previous exercise(s) a graphical interface. You
# should have Entrys for the input and output file names and a button for
# each sorting order. Bonus: Allow the user to do multiple sorts and add a
# button for quitting.

import graphics

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = graphics.Point(self.xmin, self.ymin)
        p2 = graphics.Point(self.xmax, self.ymax)
        self.rect = graphics.Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = graphics.Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()
    
    def setLabel(self, label):
        self.label.setText(label)

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

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
            
def printStudents(students, studentsTable):
    studentsTable.setText("")
    text = f"{'Name':<30} {'Hours':<10} {'QPoints':<10} {'GPA':<10}\n"
    for s in students:
        text = text + f"{s.getName():<30} {s.getHours():<10} {s.getQPoints():<10} {s.gpa():<10.2f}\n"
    studentsTable.setText(text)
            
def main():
    win = graphics.GraphWin("Students DB", 800, 600)
    win.setCoords(0, 0, 800, 600)

    quitButton = Button(win, graphics.Point(780, 10), 40, 20, "Quit")
    quitButton.activate()

    fileText = graphics.Text(graphics.Point(35, 580), "Data File:")
    fileText.draw(win)
    fileEntry = graphics.Entry(graphics.Point(175, 580), 20)
    fileEntry.setText("students.dat")
    fileEntry.draw(win)
    loadButton = Button(win, graphics.Point(300, 580), 50, 20, "Load")
    loadButton.activate()
    outputText = graphics.Text(graphics.Point(35, 550), "Output:")
    outputText.draw(win)
    outputEntry = graphics.Entry(graphics.Point(175, 550), 20)
    outputEntry.draw(win)
    saveButton = Button(win, graphics.Point(300, 550), 50, 20, "Save")

    sortByText = graphics.Text(graphics.Point(35, 520), "Sort:")
    sortByText.draw(win)
    sortByButton = Button(win, graphics.Point(110, 520), 60, 20, "GPA")
    ascButton = Button(win, graphics.Point(200, 520), 60, 20, "Asc")

    studentsText = graphics.Text(graphics.Point(35, 490), "Students")
    studentsText.draw(win)
    studentsTable = graphics.Text(graphics.Point(400, 300), "")
    studentsTable.setFace("courier")
    studentsTable.draw(win)

    students = []
    while True:
        pt = win.getMouse()
        if quitButton.clicked(pt):
            break
        elif loadButton.clicked(pt):
            if fileEntry.getText() != "":
                students = readStudents(fileEntry.getText())
                saveButton.activate()
                sortByButton.setLabel("GPA")
                ascButton.setLabel("Asc")
                students.sort(key=Student.gpa)
                sortByButton.activate()
                ascButton.activate()
                printStudents(students, studentsTable)
        elif saveButton.clicked(pt):
            if outputEntry.getText() != "":
                writeStudents(students, outputEntry.getText())
        elif sortByButton.clicked(pt):
            if sortByButton.getLabel() == "GPA":
                sortByButton.setLabel("Name")
                students.sort(key=Student.getName)
            elif sortByButton.getLabel() == "Name":
                sortByButton.setLabel("Credits")
                students.sort(key=Student.getHours)
            elif sortByButton.getLabel() == "Credits":
                sortByButton.setLabel("GPA")
                students.sort(key=Student.gpa)
            if ascButton.getLabel() == "Dec":
                students.reverse()
            printStudents(students, studentsTable)
        elif ascButton.clicked(pt):
            if ascButton.getLabel() == "Asc":
                ascButton.setLabel("Dec")
                students.reverse()
            elif ascButton.getLabel() == "Dec":
                ascButton.setLabel("Asc")
                students.reverse()
            printStudents(students, studentsTable)
    win.close()

main()
