# Review Questions

# True/False
# 1.    A simple decision can be implemented with an if statement.      True
# 2.    In Python conditions, not equals is written as /=.              False
# 3.    Strings are compared by lexicographic ordering.                 True
# 4.    A two-way decision is implemented using an if-elif statement.   False
# 5.    The math.sqrt function cannot compute the square root of a
#       negative number.                                                True
# 6.    A single try statement can catch multiple kinds of errors.      True
# 7.    Multi-way decisions must be handled by nesting multiple if-else
#       statements.                                                     False
# 8.    There is usually only one correct solution to a problem
#       involving decision structures.                                  False
# 9.    The condition x <= y <= z is allowed in Python.                 True
# 10.   Input validation means prompting a user when input is required. False

# Multiple Choice
# 1.    A statement that controls the execution of other statements is called a
#       a) boss structure
#       b) super structure
#     X c) control structure
#       d) branch
# 2.    The best structure for implementing a multi-way decision in Python is
#       a) if
#       b) if-else
#     X c) if-elif-else
#       d) try
# 3.    An expression that evaluates to either true or false is called
#       a) operational
#     X b) Boolean 
#       c) simple
#       d) compound
# 4.    When a program is being run directly (not imported), the value of
#       __name__ is
#       a) script
#       b) main 
#     X c) __main__
#       d) True
# 5.    The literals for type bool are
#       a) T,F
#     X b) True, False 
#       c) true, false
#       d) 1,0
# 6.    Placing a decision inside of another decision is an example of
#       a) cloning
#       b) spooning
#     X c) nesting
#       d) procrastination
# 7.    In Python, the body of a decision is indicated by
#     X a) indentation
#       b) parentheses 
#       c) curly braces
#       d) a colon
# 8.    A structure in which one decision leads to another set of decisions,
#       which leads to another set of decisions, etc., is called a decision
#       a) network
#       b) web
#     X c) tree
#       d) trap
# 9.    Taking the square root of a negative value with math.sqrt produces a(n)
#     X a) ValueError
#       b) imaginary number
#       c) program crash
#       d) stomachache
# 10.   A multiple choice question is most similar to a/an
#       a) simple decision
#       b) two-way decision
#     X c) multi-way decision
#       d) exception handler

# Discussion
# 1.    Explain the following patterns in your own words:
#       a) simple decision          - single if
#       b) two-way decision         - if-else
#       c) multi-way decision       - if-elif-else
# 2.    How is exception handling using try/except similar to and different
#       from handling exceptional cases using ordinary decision structures
#       (variations on if)?
#       Similar structure but can be used to handle expected errors from called functions.
# 3.    The following is a (silly) decision structure:
#           if a > b:
#               if b > c:
#                   print("Spam Please!")
#               else:
#                   print("It's a late parrot!")
#           elif b > c:
#               print("Cheese Shoppe")
#               if a >=c:
#                   print ("Cheddar")
#               elif a < b:
#                   print("Gouda")
#               elif c == b:
#                   print("Swiss")
#           else:
#               print("Trees")
#               if a == b:
#                   print ("Chestnut")
#               else:
#                   print("Larch")
#           print ("Done")
#       Show the output that would result from each of the following possible
#       values of a, b, and c respectively:
#       a) 3, 4, 5          Trees
#                           Larch
#                           Done
#       b) 3, 3, 3          Trees
#                           Chestnut
#                           Done
#       c) 5, 4, 3          Spam Please!
#                           Done
#       d) 3, 5, 2          Cheese Shoppe
#                           Cheddar
#                           Done
#       e) 5, 4, 7          It's a late parrot
#                           Done
#       f) 3, 3, 2          Cheese Shoppe
#                           Cheddar
#                           Done
