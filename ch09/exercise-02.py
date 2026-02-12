# Some languages do not have the flexible built-in list (array) operations
# that Python has. Write an algorithm for each of the following Python
# operations and test your algorithm by coding it up in a suitable function.
# For example, as a function, reverse(myList) should do the same as
# myList.reverse(). Obviously, you are not allowed to use the corresponding
# Python method to implement your function.
# a) count(myList, x) (like myList.count(x))
# b) isin(myList, x) (like x in myList))
# c) index(myList, x) (like myList.index(x))
# d) reverse(myList) (like myList.reverse())
# e) sort(myList) (like myList.sort())

def count(myList, x):
    total = 0
    for i in myList:
        if i == x:
            total = total + 1
    return total

def isin(myList, x):
    for i in myList:
        if i == x:
            return True
    return False

def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x:
            return i
    raise ValueError(f"'{x}' is not in list")

def reverse(myList):
    i = 0
    j = len(myList) - 1
    while i < j:
        myList[i], myList[j] = myList[j], myList[i]
        i = i + 1
        j = j - 1

def sort(myList):
    if len(myList) == 0 or len(myList) == 1:
        return
    # Find the biggest item in the list
    biggest_index = 0
    for i in range(1, len(myList)):
        if myList[i] > myList[biggest_index]:
            biggest_index = i
    biggest = myList.pop(biggest_index)
    # Sort the rest of the list
    sort(myList)
    # Add biggest item to the end
    myList.append(biggest)