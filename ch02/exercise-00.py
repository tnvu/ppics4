# Review Questions:

# True/False
# 1.    The best way to write a program is to immediately type in some
#       code and then debug it until it works.                              False
# 2.    An algorithm can be written without using a programming language    True
# 3.    Programs no longer require modification after they are written
#       and debugged.                                                       False
# 4.    Python identifiers must start with a letter or underscore.          True
# 5.    Keywords make good variable names.                                  False
# 6.    Expressions are built from literals, variables, and operators.      True
# 7.    In Python, x = x +1 is a legal statement.                           True
# 8.    The functions int and float are used to turn user inputs into
#       numbers.                                                            True
# 9.    A counted loop is designated to iterate a specific number a times.  True
# 10.   In a flowchart, diamonds are used to show statement sequences, and
#       rectangles are used for decision points.                            False

# Multiple Choise
# 1.    Which of the follow is /not/ a step in the software development process?
#       a) specification
#       b) testing/debugging
#     X c) fee setting
#       d) maintenance
# 2.    What is the correct forumula for converting Celsius to Fahrenheit?
#     X a) F = 9/5(C) + 32
#       b) F = 5/9(C) - 32
#       c) F = B**2 - 4AC
#       d) F = (212 - 32) / (100 - 0)
# 3.    The process of describing exactly /what/ a computer program will do
#       to solve a problem is called
#     X a) design
#       b) implementation
#       c) programming
#       d) specification
# 4.    Which of the following it /not/ a legal identifier?
#       a) spam
#       b) spAm
#     X c) 2spam
#       d) spam4U
# 5.    Which of the following are /not/ used in expressions?
#       a) variables
#     X b) statements
#       c) operators
#       d) literals
# 6.    Fragments of code that produce or calculate new data values are called
#       a) identifiers
#     X b) expressions
#       c) productive clauses
#       d) assignment statements
# 7.    Which of the following is /not/ a part of the IPO pattern?
#       a) input
#     X b) program
#       c) process
#       d) output
# 8.    The template for <variable> in range(<expr>) describes
#       a) a general for loop
#       b) an assignment statement
#       c) a flowchart
#     X d) a counted loop
# 9.    Which of the following is the most accurate model of assignment in Python?
#     X a) sticky note
#       b) variable-as-box
#       c) simultaneous
#       d) plastic-scale
# 10.   In Python, getting user input is done with a special expression called
#       a) for
#       b) read
#       c) simultaneous assignment
#     X d) input

# Discussion
# 1.    List and describe in your own words the six steps in the software
#       development process.
#       1. Problem Analysis: Studying the problem to be solved.
#       2. Program Specification: Deciding exactly what the program will do.
#       3. Design: Writing an algorithm in pseudocode.
#       4. Implementation: Translating the design into a programming language.
#       5. Testing/Debugging: Finding and fixing errors in the program.
#       6. Maintenance: Keeping the program up to date with evolving needs.
# 2.    Write out the chaos.py program (Section 1.7) and identify the parts of
#       the program as follows:
#           * Circle each identifier
#           * Underline each expression
#           * Put a comment at the ne of each line indicating the type of
#             statement on that line (output, assignment, input, loop, etc).
#       # identifier main, definition
#       def main():
#           # output
#           print("This program illustrates a chaotic function")
#           # identifier x, assignment, input
#           x = float(input("Enter a number between 0 and 1: "))
#           # identifier i, assignment, loop
#           for i in range(10):
#               # assignment
#               x = 3.9 * x * (1 - x)
#               # output
#               print(x)
# 3.    Explain the relationships among these concepts: definite loop, for
#       loop, and counted loop.
#       definite loops are loops that are executed a known number of times.
#       for statement is a definite loop that iterates through a sequences
#       of values
#       counted loop is a loop designed specifically for the purpose of 
#       repeating some portion of the program a specific number of times
# 4.    Show the output from the following fragments:
#       a)  for i in range(5):
#               print(i * i)
#           0
#           1
#           4
#           9
#           16
#       b)  for d in [3, 1, 4, 1, 5]:
#               print(d, end=" ")
#           3 1 4 1 5
#       c)  for i in range(4):
#               print("Hello")
#           Hello
#           Hello
#           Hello
#           Hello
#       d)  for i in range(5):
#               print(i, 2**i)
#           0 1
#           1 2
#           2 4
#           3 8
#           4 16
# 5.    Why is it a good idea to first write out an alogirthm in pseudocode
#       rather than jumping immediately to Python code?
#       Don't get bogged down in the details of the langauge.
# 6.    The Python print function supports other keyword parameters besides 
#       end. One of these other keyword parameters is sep. What do you think 
#       the sep parameter does? /Hint:/ sep is short for separator. Test your
#       idea either by trying in interactively for by consulting the Python
#       documentation (you can type help(print) in the Python shell or look
#       online at https://docs.python.org).
#       sep specifies the seperator between each paramenter
# 7.    What do you think will happen if the following code is executed?
#
#       print("start")
#       for i in range(0):
#           print("Hello")
#       print("end")
#       
#       Look at the flowchart for the for statement in Figure 2.3 to help you
#       figure this out. Then test your prediction by trying out these lines
#       in a program.
#       It will print:
#           start
#           end