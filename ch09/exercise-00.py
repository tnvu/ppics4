# Review Questions

# True/False
# 1.    The median is the average of a set of data.                     False
# 2.    Standard deviation measures how spread out a data set is.       True
# 3.    Arrays are usually heterogeneous, but lists are homogeneous.    False
# 4.    A Python list cannot grow and shrink in size.                   False
# 5.    Python lists are not mutable.                                   False
# 6.    A list must contain at least one item.                          False
# 7.    Items can be removed from a list with the pop operation.        True
# 8.    A tuple is like an immutable list.                              True
# 9.    A list comprehension is an expression that creates a list from
#       a sequence.                                                     True
# 10.   A Python dictionary is a kind of sequence.                      False

# Multiple Choice
# 1.    Where mathematicians use subscripting, computer programmers use
#       a) slicing
#     X b) indexing
#       c) Python
#       d) caffeine
# 2.    Which of the following is not a built-in sequence operation in Python?
#     X a) extending
#       b) concatenation
#       c) slicing
#       d) repetition
# 3.    The method that adds a single item to the end of a list is
#       a) extend
#       b) add
#       c) plus
#     X d) append
# 4.    Which of the following is not a Python list method?
#       a) index
#       b) insert
#     X c) get
#       d) pop
# 5.    Which of the following is not a characteristic of a Python list?
#       a) It is an object.
#       b) It is a sequence.
#       c) It can hold objects.
#     X d) It is immutable.
# 6.    Which of the following expressions correctly tests whether x is even?
#     X a) x % 2 == 0
#       b) even(x)
#       c) not odd(x)
#       d) x % 2 == x
# 7.    The parameter xbar in stdDev is what?
#       a) median
#       b) mode
#       c) spread
#     X d) mean
# 8.    Which property of a list does not apply to a tuple?
#       a) it can contain arbitrary values
#       b) it is a sequence
#       c) it can be indexed
#     X d) it can grow and shrink
# 9.    What “brackets” are used to build a tuple?
#     X a) ()
#       b) {}
#       c) <>
#       d) []
# 10.   What “brackets” are used to build a dictionary?
#       a) ()
#     X b) {}
#       c) <>
#       d) []

# Discussion
# 1.    Given the initial statements
#           s1 = [2, 1, 4, 3]
#           s2 = ["c", "a", "b"]
#       show the result of evaluating each of the following sequence
#       expressions:
#       a) s1 + s2
#           [2, 1, 4, 3, "c", "a", "b"]
#       b) 3 * s1 + 2 * s2
#           [2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, "c", "a", "b", "c", "a", "b"]
#       c) s1[1]
#           1
#       d) s1[1:3]
#           [1, 4]
#       e) s1 + s2[-1]
#           TypeError: can only concatenate list (not "str") to list
# 2.    Given the same initial statements as in the previous problem, show the
#       values of s1 and s2 after executing each of the following statements.
#       Treat each part independently (i.e., assume that s1 and s2 start with
#       their original values each time).
#       a) s1.remove(2)
#           s1 = [1, 4, 3]
#       b) s1.sort()
#           s1 = [1, 2, 3, 4]
#       c) s1.append([s2.index("b")])
#           s1 = [2, 1, 4, 3, [2]]
#       d) s2.pop(s1.pop(0))
#           s1 = [1, 4, 3]
#           s2 = ["c", "a"]
#       e) s2.insert(s1[1], "d")
#           s2 = ["c", "d", "a", "b"]
# 3.    Write list comprehensions to produce the same lists that are produced by
#       the following accumulator loops:
#       a)  lst = []
#           for num in range(1000):
#               lst.append(num ** 3)
#           lst = [num ** 3 for num in range(1000)]
#       b)  lst = []
#           for x in inStr.split(","):
#               lst.append(float(x))
#           lst = [float(x) for x in inStr.split(",")]
#       c)  lst =[]
#           for word in inStr.split():
#               if len(word) != 4:
#                   lst.append(word)
#           lst = [word for word in inStr.split() if len(word) != 4]
#       d) lst = []
#           for word in sentence:
#               if len(word) == 4:
#                   lst.append(word.upper())
#           lst = [word.upper() for word in sentence if len(word) == 4]
#       e)  evens = []
#           odds = []
#           for num in data:
#               if num % 2 == 0:
#                   evens.append(num)
#               else:
#                   odds.append(num)
#           evens = [num for num in data if num % 2 == 0]
#           odds = [num for num in data if num % 2 == 1]
# 4.    A list comprehension followed by a string join operation can be a 
#       convenient alternative to a string accumulator loop. Rewrite the 
#       following loops using that approach:
#       a)  result = ""
#           for ch in msg:
#               result = result + chr(ord(ch) + 1)
#           result = "".join([chr(ord(ch) + 1) for ch in msg])
#       b)  result = ""
#           for word in msg.split():
#               result = result + translate(word) + " "
#           result = result[:-1] # take extra space off the end
#           result = " ".join([translate(word) for word in msg.split()])
