# Write a suite of functions to implement mathematical set operations.
# makeSet(elements) Returns a list containing all of the items in elements,
# but without any duplicates.
# addElement(s, x) Adds x to s if it is not already in s; otherwise, s is left
# unchanged.
# deleteElement(s, x) Removes x from s, if present; otherwise, s is left
# unchanged.
# member(s, x) Returns True if x is in s, and False otherwise.
# intersection(s1, s2) Returns a new list containing just those elements
# that are common to s1 and s2.
# union(s1, s2) Returns a new list containing all of the elements that are
# in s1, s2, or both (without any duplicates).
# subtract(s1, s2) Returns a new list containing all the elements in s1
# that are not in s2.
# By the way, sets are so useful that Python actually has a built-in set
# datatype. While you may want to investigate Python’s set, you should not
# use it here. The point of this exercise is to improve your skills in
# algorithm development using lists.

def makeSet(elements):
    s = []
    for x in elements:
        addElement(s, x)
    return s

def addElement(s, x):
    if x not in s:
        s.append(x)

def deleteElement(s, x):
    if x in s:
        s.remove(x)

def member(s, x):
    return x in s

def intersection(s1, s2):
    s = []
    for x in s1:
        addElement(s, x)
    for x in s2:
        addElement(s, x)
    return s

def union(s1, s2):
    s = []
    for x in s1:
        if member(s2, x):
            s.append(x)
    return s

def subtract(s1, s2):
    s = []
    for x in s1:
        if not member(s2, x):
            s.append(x)
    return s
