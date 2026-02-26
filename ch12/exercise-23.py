# Create a class called StatSet that can be used to do simple statistical
# calculations. The methods for the class are:
#       __init__(self) Creates a StatSet with no data in it.
#       addNumber(self,x) x is a number. Adds the value x to the statSet.
#       mean(self) Returns the mean of the numbers in this statSet.
#       median(self) Returns the median of the numbers in this statSet.
#       stdDev(self) Returns the standard deviation of the numbers in this statSet.
#       count(self) Returns the count of numbers in this statSet.
#       min(self) Returns the smallest value in this statSet.
#       max(self) Returns the largest value in this statSet.
# Test your class with a program similar to the simple statistics program
# from Chapter 9.

import math
import unittest

class StatSet:
    def __init__(self):
        self.numbers = []

    def addNumber(self, x):
        self.numbers.append(x)

    def mean(self):
        return sum(self.numbers) / len(self.numbers)

    def median(self):
        self.numbers.sort()
        mid = len(self.numbers) // 2
        if len(self.numbers) % 2 == 0:
            return (self.numbers[mid-1] + self.numbers[mid]) / 2
        else:
            return self.numbers[mid]

    def stdDev(self):
        xbar = self.mean()
        sumDevSq = 0
        for n in self.numbers:
            dev = n - xbar
            sumDevSq = sumDevSq + dev**2
        return math.sqrt(sumDevSq/(len(self.numbers)-1))

    def count(self):
        return len(self.numbers)

    def min(self):
        if len(self.numbers) == 0:
            return None
        self.numbers.sort()
        return self.numbers[0]

    def max(self):
        if len(self.numbers) == 0:
            return None
        self.numbers.sort()
        return self.numbers[-1]
    
class StatSetTest(unittest.TestCase):
    def testMean(self):
        s = StatSet()
        for n in (10, 12, 23, 23, 16, 23, 21, 16):
            s.addNumber(n)
        self.assertEqual(18, s.mean())

    def testMedian(self):
        s = StatSet()
        for n in (10, 12, 23, 23, 16, 23, 21, 16):
            s.addNumber(n)
        self.assertEqual(18.5, s.median())

    def testStdDev(self):
        s = StatSet()
        for n in (10, 12, 23, 23, 16, 23, 21, 16):
            s.addNumber(n)
        self.assertAlmostEqual(5.2372293656638, s.stdDev())

    def testCount(self):
        s = StatSet()
        self.assertEqual(0, s.count())
        s.addNumber(1)
        self.assertEqual(1, s.count())
        s.addNumber(10)
        s.addNumber(10)
        s.addNumber(10)
        self.assertEqual(4, s.count())

    def testMin(self):
        s = StatSet()
        self.assertIsNone(s.min())
        s.addNumber(123)
        self.assertEqual(123, s.min())
        s.addNumber(4)
        self.assertEqual(4, s.min())
        s.addNumber(1000)
        self.assertEqual(4, s.min())

    def testMax(self):
        s = StatSet()
        self.assertIsNone(s.max())
        s.addNumber(123)
        self.assertEqual(123, s.max())
        s.addNumber(4)
        self.assertEqual(123, s.max())
        s.addNumber(1000)
        self.assertEqual(1000, s.max())


    
if __name__ == '__main__':
    unittest.main()