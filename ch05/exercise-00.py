# Review Questions

# True/False
# 1.    Programmers rarely define their own functions.                  False
# 2.    A function may only be called at one place in a program.        False
# 3.    Information can be passed into a function through parameters.   True
# 4.    Every Python function must have a return statement.             False
# 5.    In Python, some parameters are passed by reference.             False
# 6.    In Python, a function can return only one value.                False
# 7.    Python functions can never modify a parameter.                  True
# 8.    One reason to use functions is to reduce code duplication.      True
# 9.    Variables defined in a function are local to that function.     True
# 10.   It's generally a bad idea to define new functions if it makes
#       a program longer.                                               False

# Multiple Choice
# 1.    The part of a program that uses a function is called the
#       a) user
#     X b) caller
#       c) callee
#       d) statement
# 2.    A Python function definition begins with
#     X a) def
#       b) define
#       c) function
#       d) defun
# 3.    A function can send output back to the program with a(n)
#     X a) return
#       b) print
#       c) assignment
#       d) SASE
# 4.    Formal and actual parameters are matched up by
#       a) type
#     X b) position
#       c) ID
#       d) interests
# 5.    Which of the following is not a step in the function-calling process?
#       a) The calling program suspends.
#       b) The formal parameters are assigned the value of the actual parameters.
#       c) The body of the function executes.
#     X d) Control returns to the point just before the function was called.
# 6.    In Python, actual parameters are passed to functions
#     X a) by value
#       b) by reference
#       c) at random
#       d) by networking
# 7.    Which of the following is not a reason to use functions?
#       a) to reduce code duplication
#       b) to make a program more modular
#       c) to make a program more self-documenting
#     X d) to demonstrate intellectual superiority
# 8.    If a function returns a value, it should generally be called from
#     X a) an expression
#       b) a different program
#       c) main
#       d) a cell phone
# 9.    A function with no return statement returns
#       a) nothing
#       b) its parameters
#       c) its variables
#     X d) None
# 10.   A function can modify the value of an actual parameter only if it’s
#     X a) mutable
#       b) a list
#       c) passed by reference
#       d) a variable

# Discussion
# 1.    In your own words, describe the two motivations for defining functions
#       in your programs.
#       * Reduce code duplication
#       * Simplify code by giving names to common operations
# 2.    We have been thinking about computer programs as sequences of
#       instructions where the computer methodically executes one instruction
#       and then moves on to the next one. Do programs that contain functions
#       fit this model? Explain your answer.
#       No because execution of instructions halt and then jumps to the
#       function being called before returning to the instruction after the
#       function was called.
# 3.    Parameters are an important concept in defining functions.
#       a) What is the purpose of parameters?
#       Pass information to the function
#       b) What is the difference between a formal parameter and an actual
#          parameter?
#       Formal parameters appear in the function definition.
#       Actual parameters are expressions that appear in a function call.
#       c) In what ways are parameters similar to and different from ordinary
#          variables?
#       They exist only local to the function
# 4.    Functions can be thought of as miniature (sub)programs inside other
#       programs. Like any other program, we can think of functions as having
#       input and output to communicate with the main program.
#       a) How does a program provide “input” to one of its functions?
#       Through parameters
#       b) How does a function provide “output” to the program?
#       Through return statement
# 5.    Consider this very simple function:
#           def cube(x):
#               answer = x * x * x
#               return answer
#       a) What does this function do?
#       Calculates the cube of x.
#       b) Show how a program could use this function to print the value 
#          of y^3, assuming y is a variable.
#       print(cube(y))
#       c) Here is a fragment of a program that uses this function:
#           answer = 4
#           result = cube(3)
#           print(answer, result)
#       The output from this fragment is 4 27. Explain why the output is not
#       27 27, even though cube seems to change the value of answer to 27.
#       The variable 'answer' in the cube function is only in the scope of the
#       cube function and does not affect other variables also names 'answer'
#       outside of it's scope.