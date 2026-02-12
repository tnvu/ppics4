# A blood pressure reading is considered normal if the systolic pressure is
# less than 120 and the diastolic pressure is less than 80. Write a function
# that takes a set of blood pressure readings represented as a list of (systolic,
# diastolic) tuples and returns two lists, one containing the normal readings
# and the other containing the elevated readings.

import unittest

def sortBloodPressures(bps):
    normal = [bp for bp in bps if bp[0] < 120 and bp[1] < 80]
    elevated = [bp for bp in bps if bp[0] >= 120 or bp[1] >= 80]
    return normal, elevated

class TestSortBloodPressure(unittest.TestCase):
    bps = [(110, 65), (115, 75), (145, 60), (120, 100)]
    normal, elevated = sortBloodPressures(bps)
    
    def testSortBloodPressures(self):
        self.assertListEqual([(110, 65), (115, 75)], self.normal)
        self.assertListEqual([(145, 60), (120, 100)], self.elevated)

if __name__ == '__main__':
    unittest.main()