# Review Questions

# True/False
# 1.    New objects are created by invoking a constructor.              True
# 2.    Functions that live in objects are called instance variables.   False
# 3.    The first parameter of a Python method definition is called
#       this.                                                           False
# 4.    An object can have at most one instance variable.               False
# 5.    In data processing, a collection of information about a person
#       or thing is called a file.                                      False
# 6.    In a Python class, the constructor is called __init__.          True
# 7.    A docstring is the same thing as a comment.                     False
# 8.    Instance variables go away once a method terminates.            False
# 9.    Method names should always begin with one or two underscores.   False
# 10.   An application should not be considered an object.              False

# Multiple Choice
# 1.    What Python reserved word starts a class definition?
#       a) def 
#     X b) class
#       c) object
#       d) __init__
# 2.    A method definition with four formal parameters is generally called with
#       how many actual parameters?
#     X a) three
#       b) four
#       c) five
#       d) it depends
# 3.    A method definition is similar to a(n)
#       a) loop
#       b) module
#       c) import statement
#     X d) function definition
# 4.    Within a method definition, the instance variable x could be accessed via
#       which expression?
#       a) x
#     X b) self.x
#       c) self[x]
#       d) self.getX()
# 5.    A Python convention for defining methods that are “private” to a class
#       is to begin the method name with
#       a) “private”
#       b) a pound sign (#)
#     X c) an underscore (_)
#       d) a hyphen (-)
# 6.    The term applied to hiding details inside class definitions is
#       a) obscuring
#       b) subclassing
#       c) documentation
#     X d) encapsulation
# 7.    A Python string literal can span multiple lines if enclosed with
#       a) "
#       b) '
#     X c) """
#       d) \
# 8.    In a Button widget, what is the data type of the instance variable
#       active?
#     X a) bool
#       b) int
#       c) float
#       d) str
# 9.    Which of the following methods is part of the DieView class in this 
#       chapter?
#       a) activate
#       b) setColor
#     X c) setValue
#       d) clicked
# 10.   What keyword parameter is used to send a key-function to the sort 
#       method?
#       a) reverse
#       b) reversed
#     X c) cmp
#       d) key

# Discussion
# 1.    Explain the similarities and differences between instance variables and
#       “regular” function variables.
#       Instance variables are alive for the duration of the instance while function
#       variables are alive during the running of the function. You cannot access
#       function variables from other parts of code.
# 2.    Explain the following in terms of actual code that might be found in a class
#       definition:
#       a) method
#           Used to access/modify the instance
#       b) instance variable
#           Variable used to hold information about an instance
#       c) constructor
#           Initializes the instance
#       d) accessor
#           Accesses the instance variables through a common interface
#       e) mutator
#           Modify the instance variables through a common interface
# 3.    Show the output that would result from the following nonsense program:
#           class Bozo:
#               def __init__(self, value):
#                   print("Creating a Bozo from:", value)
#                   self.value = 2 * value
#               def clown(self, x):
#                   print("Clowning:", x)
#                   print(x * self.value)
#                   return x + self.value
#
#           def main():
#               print("Clowning around now.")
#               cl = Bozo(3)
#               c2 = Bozo(4)
#               print c1.clown(3)
#               print c2.clown(cl.clown(2))
#
#           main()
#
#           Clowning around now.
#           Creating a Bozo from 3
#           Creating a Bozo from 4
#           Clowning: 3
#           18
#           9
#           Clowning: 2
#           12
#           Clowning: 8
#           64
#           16
