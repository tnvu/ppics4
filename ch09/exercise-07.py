# Use the functions from the previous two exercises to write a program that
# computes the sum of the squares of numbers that the user enters on a
# single line of input.

### COPIED FROM CH09 EXERCISE 05 ###
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

### COPIED FROM CH09 EXERCISE 06 ###
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def main():
    nums = input("Enter a list of numbers separated by spaces: ").split()
    toNumbers(nums)
    squareEach(nums)
    print(f'Sum of squares = {sum(nums)}')

main()

