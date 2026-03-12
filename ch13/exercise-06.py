# Write a program to keep track of conference attendees. For each attendee,
# your program should keep track of name, company, state, and email address.
# Your program should allow users to do things such as add a new attendee, 
# display information on an attendee, delete an attendee, list the names and 
# email addresses of all attendees, and list the names and email addresses of
# all attendees from a given state. The attendee list should be stored in a 
# file and loaded when the program starts.

import pickle

class Attendee:
    def __init__(self, name, company, state, email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email

class AttendeeTracker:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename, "rb") as infile:
                self.attendees = pickle.load(infile)
        except FileNotFoundError:
            self.attendees = []

    def close(self):
        with open(self.filename, "wb") as outfile:
            pickle.dump(self.attendees, outfile)

    def addAttendee(self, name, company, state, email):
        attendee = Attendee(name, company, state, email)
        self.attendees.append(attendee)
        
    def showAttendee(self, name):
        for attendee in self.attendees:
            if attendee.name == name:
                return attendee
        return None

    def deleteAttendee(self, name):
        for attendee in self.attendees[:]:
            if attendee.name == name:
                self.attendees.remove(attendee)

    def listAttendees(self):
        return self.attendees[:]

    def listAttendeesFromState(self, state):
        attendees = []
        for attendee in self.attendees:
            if attendee.state == state:
                attendees.append(attendee)
        return attendees

class AttendeeTrackerApp:
    def __init__(self, filename):
        self.tracker = AttendeeTracker(filename)

    def run(self):
        while True:
            cmd = input("Commands - (A)=add attendee, (S)=show attendee, (D)=delete attendee, " +
                        "(L)=list attendees, (LS)=list attendees from state, (Q)=quit: ")
            if cmd in ['a', 'A']:
                self.addAttendee()
            elif cmd in ['s', 'S']:
                self.showAttendee()
            elif cmd in ['d', 'D']:
                self.deleteAttendee()
            elif cmd in ['l', 'L']:
                self.listAttendees()
            elif cmd in ['ls', 'LS']:
                self.listAttendeesState()
            elif cmd in ['q', 'Q']:
                break
        self.tracker.close()

    def addAttendee(self):
        name = input("Name: ")
        company = input("Company: ")
        state = input("State: ")
        email = input("Email: ")
        self.tracker.addAttendee(name, company, state, email)

    def showAttendee(self):
        name = input("Name: ")
        attendee = self.tracker.showAttendee(name)
        if attendee:
            self.printAttendees([attendee])
        else:
            print(f"Not Found: {name}")

    def deleteAttendee(self):
        name = input("Name: ")
        self.tracker.deleteAttendee(name)

    def listAttendees(self):
        for attendee in self.tracker.listAttendees():
            self.printAttendees([attendee])

    def listAttendeesState(self):
        state = input("State: ")
        for attendee in self.tracker.listAttendeesFromState(state):
            self.printAttendees([attendee])

    def printAttendees(self, attendees):
        name_header = "NAME"
        company_header = "COMPANY"
        state_header = "STATE"
        email_header = "EMAIL"
        print(f"{name_header:15} {company_header:15} {state_header:15} {email_header:15}")
        if len(attendees) == 0:
            print("No attendees")
            return
        for attendee in attendees:
            print(f'{attendee.name:15} {attendee.company:15} {attendee.state:15} {attendee.email:15}')

def main():
    filename = input("Attendee database: ")
    AttendeeTrackerApp(filename).run()

main()