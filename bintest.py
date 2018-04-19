import binsearch as roman
import unittest
class KnownValues(unittest.TestCase): # (1)
    knownValues = (([1,2,3,4,5],1,1),
                   ([1,2,3,4,5],2,2),
                   ([1,2,3,4,5],3,3),
                   ([1,2,3,4,5],4,4),
                   ([1,2,3,4,5],5,5),
                   ([1,2,3,4],1,1),
                   ([1,2,3,4],2,2),
                   ([1,2,3,4],3,3),
                   ([1,2,3,4],4,4),
                   ([1,2,3],1,1),
                   ([1,2,3],2,2),
                   ([1,2,3],3,3),
                   ([1,2],1,1),
                   ([1,2],2,2),
                   ([1],1,1))                   # (2)
    def testBinSearchKnown(self): # (3)
        """toRoman should give known result with known input"""
        for lst,key,resK in self.knownValues:
            res = roman.binsearch(lst,key)
            self.assertEqual(resK, res)

class BinSearchFailedInput(unittest.TestCase):
    def testNotList(self):
        """toRoman should fail with non-integer input"""
        self.assertRaises(roman.InvalidArgument, roman.binsearch, 0.5,1)

class SanityCheck(unittest.TestCase):
    def testOutOfRange(self):
        self.assertRaises(roman.InvalidIdx, roman.binsearch, [1,2,3,4],5)
    def testGoBack(self):
        a = [1,2,3,4,6,8,11,13,15,17]
        key = binSearch(a, 8)
        self.assertEqual(a[index], key)
    def testNotFound(self):
        self.assertRaises(roman.NotFound, roman.binsearch, [1,2,3,9],5)

if __name__ == "__main__":
    unittest.main()
