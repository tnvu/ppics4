# Write and test a function to meet this specification:
# squareEach(nums) nums is a list of numbers. Modifies the list by squaring
# each entry.

import unittest

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

class TestSquareEach(unittest.TestCase):
    def testSquareEach(self):
        nums = []
        squareEach(nums)
        self.assertListEqual([], nums)
        nums = [0]
        squareEach(nums)
        self.assertListEqual([0], nums)
        nums = [0, 1, 2]
        squareEach(nums)
        self.assertListEqual([0, 1, 4], nums)
        nums = [3, 4, 6, 1, 3]
        squareEach(nums)
        self.assertListEqual([9, 16, 36, 1, 9], nums)

if __name__ == '__main__':
    unittest.main()