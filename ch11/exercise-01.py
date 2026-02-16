# Write and test a function, choice (myList), that returns an item chosen at
# random from myList. By the way, the random module has this function, but the
# point of this exercise is for you to design your own algorithm based on 
# randrange and list operations.

import random
import unittest

def choice(myList):
    return myList[random.randrange(0, len(myList))]

class TestChoice(unittest.TestCase):
    def testChoice(self):
        random.seed(0)
        myList = ['c', 'a', 't', 1, 4, 3]
        self.assertEqual(choice(myList), 1)
        self.assertEqual(choice(myList), 1)
        self.assertEqual(choice(myList), 'c')
        self.assertEqual(choice(myList), 't')
        self.assertEqual(choice(myList), 4)
        self.assertEqual(choice(myList), 1)
        self.assertEqual(choice(myList), 1)
        self.assertEqual(choice(myList), 't')
        self.assertEqual(choice(myList), 1)
        self.assertEqual(choice(myList), 't')
        self.assertEqual(choice(myList), 4)
        self.assertEqual(choice(myList), 'a')
        self.assertEqual(choice(myList), 4)
        self.assertEqual(choice(myList), 'a')
        self.assertEqual(choice(myList), 't')
        self.assertEqual(choice(myList), 'a')
        self.assertEqual(choice(myList), 'c')
        self.assertEqual(choice(myList), 4)
        self.assertEqual(choice(myList), 't')
        self.assertEqual(choice(myList), 4)
        self.assertEqual(choice(myList), 3)

if __name__ == '__main__':
    unittest.main()
