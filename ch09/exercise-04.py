# Write and test a function removeDuplicates(somelist) that removes duplicate
# values from a list.

import unittest

def removeDuplicates(somelist):
    if len(somelist) == 0 or len(somelist) == 1:
        return
    last = somelist.pop()
    isUnique = True
    for i in range(len(somelist) - 1, -1, -1):
        if somelist[i] == last:
            somelist.pop(i)
            isUnique = False
    removeDuplicates(somelist)
    if isUnique:
        somelist.append(last)

class TestRemoveDuplicates(unittest.TestCase):
    def testRemoveDuplicates(self):
        somelist = []
        removeDuplicates(somelist)
        self.assertListEqual([], somelist)
        somelist = [0]
        removeDuplicates(somelist)
        self.assertListEqual([0], somelist)
        somelist = [0, 0]
        removeDuplicates(somelist)
        self.assertListEqual([], somelist)
        somelist = [0, 0, 1]
        removeDuplicates(somelist)
        self.assertListEqual([1], somelist)
        somelist = [0, 1, 0, 1, 0, 1]
        removeDuplicates(somelist)
        self.assertListEqual([], somelist)
        somelist = [0, 1, 0, 2, 0, 1]
        removeDuplicates(somelist)
        self.assertListEqual([2], somelist)
        somelist = [0, 1, 2, 3, 4, 5]
        removeDuplicates(somelist)
        self.assertListEqual([0, 1, 2, 3, 4, 5], somelist)

if __name__ == '__main__':
    unittest.main()