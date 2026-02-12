# Modify the statistics program from this chapter so that client programs
# have more flexibility in computing the mean and/or standard deviation.
# Specifically, redesign the library to have the following functions:
#       mean(nums) Returns the mean of numbers in nums.
#       stdDev(nums) Returns the standard deviation of nums.
#       meanStdDev (nums) Returns both the mean and standard deviation of 
#                         nums.

import math

def mean(nums):
    total = 0
    for n in nums:
        total = total + n
    return total / len(nums)

def stdDev(nums):
    xbar = mean(nums)
    sumDevSq = 0
    for n in nums:
        dev = n - xbar
        sumDevSq = sumDevSq + dev**2
    return math.sqrt(sumDevSq/(len(nums)-1))

def meanStdDev(nums):
    return (mean(nums), stdDev(nums))
