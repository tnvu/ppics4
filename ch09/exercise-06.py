# Write and test a function to meet this specification:
# toNumbers(strList) strList isa list of strings, each of which represents
# a number. Modifies each entry in the list by converting it to a number.

import unittest

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

class TestToNumbers(unittest.TestCase):
    def testToNumbers(self):
        strList = []
        toNumbers(strList)
        self.assertListEqual([], strList)
        strList = ['0']
        toNumbers(strList)
        self.assertListEqual([0], strList)
        strList = ['0', '1']
        toNumbers(strList)
        self.assertListEqual([0, 1], strList)
        strList = ['0.5', '1.2', '3.4']
        toNumbers(strList)
        self.assertListEqual([0.5, 1.2, 3.4], strList)

if __name__ == '__main__':
    unittest.main()