# Write and test a function shuffle(myList) that scrambles a list into a 
# random order, like shuffling a deck of cards. By the way, the random module
# has this function, but the point of this exercise is for you to design your
# own algorithm based on randrange and list operations.

import random
import unittest

def shuffle(myList):
    for _ in range(len(myList) // 2):
        slotA = random.randrange(0, len(myList))
        slotB = random.randrange(0, len(myList))
        myList[slotA], myList[slotB] = myList[slotB], myList[slotA]

class TestShuffle(unittest.TestCase):
    def testShuffle(self):
        random.seed(0)
        myList = [1, 4, 3, 'd', 'o', 'g']
        shuffle(myList)
        self.assertEqual([3, 4, 1, 'o', 'd', 'g'], myList)
        shuffle(myList)
        self.assertEqual([3, 'd', 1, 'o', 4, 'g'], myList)
        shuffle(myList)
        self.assertEqual(['d', 1, 4, 'o', 3, 'g'], myList)

if __name__ == '__main__':
    unittest.main()