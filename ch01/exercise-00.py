# Review Questions:

# True/False
# 1.    Computer science is the study of computers.                     False
# 2.    The CPU is the "brain" of the computer.                         True
# 3.    Secondary memory is also called RAM.                            False
# 4.    All information that a computer is currently working on is
#       stored in main memory.                                          True
# 5.    The syntax of a language is its meaning, and semantics is
#       its form.                                                       False
# 6.    A function definition is a sequence of statements that
#       defines a new command.                                          True
# 7.    The software that ties all the components of a computer into
#       a usable system is called the compiler.                         False
# 8.    A subdirectory of your home directory is a good place to store
#       your Python programs.                                           True
# 9.    A variable is used to give a name to a value so it can be
#       referred to in other places.                                    True
# 10.   A chaotic function can't be computed by a computer.             False

# Multiple Choice
# 1.    What is the fundamental question of computer science?
#       a) How fast can a computer compute?
#     X b) What can be computed?
#       c) What is the most efficient programming language?
#       d) How much money can a programmer make?
# 2.    An algorithm is like a
#       a) newspaper
#       b) venus flytrap
#       c) drum
#     X d) recipe
# 3.    Which of the following is /not/ an example of secondary memory?
#     X a) RAM
#       b) hard drive
#       c) USB flash drive
#       d) DVD
# 4.    Which of the following is not an example of an operating system?
#       a) Windows
#       b) MacOS
#     X c) IDLE
#       d) Linux
# 5.    A file extension indicates
#     X a) the type of data stored in the file
#       b) where the file is located
#       c) how to make the file longer
#       d) who the file belongs to
# 6.    Computer langauges are designed to be used and understood by humans are
#       a) natural langauges
#     X b) high-level computer langauges
#       c) machine langauges
#       d) fetch-execute langauges
# 7.    A statement is
#       a) a translation of machine language
#     X b) a complete computer command
#       c) a precise description of a problem
#       d) a section of an algorithm
# 8.    One difference between a compiler and an interpreter is
#       a) a compiler is a program
#       b) a compiler is used to translate high-level language into machine
#          language
#     X c) a compiler is no longer needed after a program is translated
#       d) a compiler processes source code
# 9.    By convention, the statements of a program are often placed in a
#       function called
#       a) import
#     X b) main
#       c) program
#       d) IDLE
# 10.   The items listed in the parentheses of a function definition are called
#       a) parenthicals
#       b) parameters
#       c) arguments
#     X d) both b) and c) are correct

# Discussion
# 1.    Compare and contrast the following pairs of concepts from the chapter:
#       a) Hardware vs Software
#          Hardware is the physical components of the computer
#          Software is the instructions to be run on the computer
#       b) Algorithm vs Program
#          Algorithm is a recipe to solve a problem
#          Program is the implementation of the algorithm
#       c) Programming Language vs Natural Language
#          Programming languages are used to tell what computers to do
#          Natural languages are spoken between people
#       d) High-Level Langauge vs Machine Language
#          High-level languages are easier understood by programmers
#          Machine language is the specfic codes used by specific CPUs
#       e) Interpreter vs Compiler
#          Interpreters translate source code to machine language each time the
#          program is run
#          Compilers translate source code to machine language a single time
#       f) Syntax vs Semantics
#          Syntax is the rules of the programming language
#          Semantics is the meaning of the statements in a programming langauge
# 2.    List and explain in your own words the role of each of the five basic 
#       functional units of a computer depicted in Figure 1.1
#       Input devices - where the user gives the computer information
#       CPU - the brains of the computer
#       Main memory - the working area of the CPU
#       Output devices - where the user receives the computer information
#       Secondary memory - non-volatile memory for computers
# 3.    Write a detailed algorithm for making a peanut butter and jelly 
#       sandwich (or some other everyday activity). You should assume that you
#       are talking to someone who is conceptually able to do the task but has
#       never actually done it before. For example, you might be telling a
#       young child.
#       1. Get bread
#       2. Get peanut butter
#       3. Get jelly
#       4. Get 2 spoons
#       5. While not enough peanut butter:
#           a. Scoop peanut butter
#           b. Spread peanut butter onto bread
#       6. While not enough jelly:
#           a. Scoop jelly
#           b. Spread jelly onto bread
#       7. Put peanut butter side and jelly sides of bread together
# 4.    As you learn in a later chapter, many of the numbers stored in a 
#       computer are not exact values, but rather close approximations. For
#       example, the value 0.1 might be stored as 0.10000000000000000555.
#       Usually, such small difference are not a problem; however, given what
#       you have learned about chaotic behavior in Chapter 1, you should
#       realize the need for caution in certain situations. Can you think of
#       examples where this might be a problem? Explain.
#       Long distance calculations where a little bit off in the initial
#       conditions can cause disastrous effects.
# 5.    Trace through the chaos program from Section 1.7 by hand using 0.15 as
#       the input value. Show the sequence of output that results.
#       x = 0.15
#       x = 3.9 * 0.15 * (1 - 0.15) = 0.49724999999999997
#       x = 3.9 * 0.49724999999999997 * (1 - 0.49724999999999997)
#         = 0.97497050625
#       x = 3.9 * 0.97497050625 * (1 - 0.97497050625)
#         = 0.09517177095121285
#       x = 3.9 * 0.09517177095121285 * (1 - 0.09517177095121285)
#         = 0.3358450093643686
#       x = 3.9 * 0.3358450093643686 * (1 - 0.3358450093643686)
#         = 0.8699072422927216
#       x = 3.9 * 0.8699072422927216 * (1 - 0.8699072422927216)
#         = 0.4413576651876355
#       x = 3.9 * 0.4413576651876355 * (1 - 0.4413576651876355)
#         = 0.9615881986142427
#       x = 3.9 * 0.9615881986142427 * (1 - 0.9615881986142427)
#         = 0.14405170611022783
#       x = 3.9 * 0.14405170611022783 * (1 - 0.14405170611022783)
#         = 0.48087316710014555
#       x = 3.9 * 0.48087316710014555 * (1 - 0.48087316710014555)
#         = 0.9735732406265619