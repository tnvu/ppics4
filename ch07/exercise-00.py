# Review Questions

# True/False
# 1.    A Python while implements a definite loop.                      False
# 2.    The counted loop pattern uses a definite loop.                  True
# 3.    A sentinel loop asks the user whether to continue on each
#       iteration.                                                      False
# 4.    A sentinel loop should not actually process the sentinel
#       value.                                                          True
# 5.    The checkMouse method does not wait for the user to click the
#       mouse.                                                          True
# 6.    A while is a post-test loop.                                    False
# 7.    The Boolean operator or returns True when both of its operands
#       are true.                                                       False
# 8.    a and (b or c) == (a and b) or (a and c)                        True
# 9.    not(a or b) == (not a) or not(b)                                False
# 10.   True or False                                                   True

# Multiple Choice
# 1.    A loop pattern that asks the user whether to continue on each 
#       iteration is called a(n)
#     X a) interactive loop
#       b) end-of-file loop
#       c) sentinel loop
#       d) infinite loop
# 2.    A loop pattern that continues until a special value is input is called
#       a(n)
#       a) interactive loop
#       b) end-of-file loop
#     X c) sentinel loop
#       d) infinite loop
# 3.    A loop structure that tests the loop condition after executing the
#       loop body is called a
#       a) pre-test loop
#       b) loop and a half
#       c) sentinel loop
#     X d) post-test loop
# 4.    A priming read is part of the pattern for a(n)
#       a) interactive loop
#       b) end-of-file loop
#     X c) sentinel loop
#       d) infinite loop
# 5.    What statement can be executed in the body of a loop to cause it to
#       terminate?
#       a) if
#       b) input
#     X c) break
#       d) exit
# 6.    Which of the following is not a valid rule of Boolean algebra?
#       a) (True or x) == True
#       b) (False and x) == False
#     X c) not(a and b) == not(a) and not(b)
#       d) (True or False) == True
# 7.    A loop that never terminates is called
#       a) busy
#       b) indefinite
#       c) tight
#     X d) infinite
# 8.    Which line would not be found in a truth table for and?
#       a) T T T
#     X b) T F T 
#       c) F T F
#       d) F F F
# 9.    Which line would not be found in a truth table for or?
#       a) T T T
#       b) T F T
#     X c) F T F
#       d) F F F
# 10.   The term for an operator that may not evaluate one of its subexpressions
#       is
#     X a) short-circuit
#       b) faulty
#       c) exclusive
#       d) indefinite

# Discussion
# 1.    Compare and contrast the following pairs of terms:
#       a) definite loop vs. indefinite loop
#       Executes a fixed number of times vs an non-fixed number of times
#       b) for loop vs. while loop
#       Definite loop vs indefinite loop
#       c) interactive loop vs. sentinel loop
#       Prompts user to continue vs looks for sentinel value to exit loop
# 2.    Give a truth table that shows the Boolean value of each of the
#       following Boolean expressions, for every possible combination of
#       “input” values.
#       Hint: Including columns for intermediate expressions is helpful.
#       a) not (P and Q)
#               P   Q   P and Q     not(P and Q)
#               T   T   T           F
#               T   F   F           T
#               F   T   F           T
#               F   F   F           T
#       b) (not P) and Q
#               P   Q   (not P)     (not P) and Q
#               T   T   F           F
#               T   F   F           F
#               F   T   T           T
#               F   F   T           F
#       c) (not P) or (not Q)
#               P   Q   (not P)     (not Q)     (not P) or (not Q)
#               T   T   F           F           F
#               T   F   F           T           T
#               F   T   T           F           T
#               F   F   T           T           T
#       d) (P and Q) or R
#               P   Q   R   (P and Q)   (P and Q) or R
#               T   T   T   T           T
#               T   T   F   T           T
#               T   F   F   F           F
#               T   F   T   F           T
#               F   T   T   F           T
#               F   T   F   F           F
#               F   F   T   F           T
#               F   F   F   F           F
#       e) (P or R) and (Q or R)
#           P   Q   R   (P or R)    (Q or R)    (P or R) and (Q or R)
#           T   T   T   T           T           T
#           T   T   F   T           T           T
#           T   F   T   T           T           T
#           T   F   F   T           F           F
#           F   T   T   T           T           T
#           F   T   F   T           T           T
#           F   F   T   T           T           T
#           F   F   F   F           F           F
# 3.    Write a while loop fragment that calculates the following values:
#       a) Sum of the first n counting numbers: 1 +2+3+...+n
#               i = 1
#               sum = 0
#               while i <= n:
#                   sum = sum + i
#                   i = i + 1
#       b) Sum of the first n odd numbers: 1 +3+5+...+2n—1
#               i = 1
#              sum = 0
#               while i <= (2n - 1):
#                   sum = sum + i
#                   i = i + 2
#       c) Sum of a series of numbers entered by the user until the value 999
#       is entered. Note: 999 should not be part of the sum.
#               sum = 0
#               while True:
#                   n = int(input("Number: "))
#                   if n == 999: break
#                   sum = sum + n
#       d) The number of times a whole number n can be divided by 2 (using
#       integer division) before reaching 1 (i.e., log2(n)).
#               count = 0
#               while True:
#                   n = n // 2
#                   if n == 0: break
#                   count = count + 1