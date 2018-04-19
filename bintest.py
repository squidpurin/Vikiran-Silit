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
        self.assertRaises(roman.InvalidArgument, roman.binsearch, (0.5,1))

class SanityCheck(unittest.TestCase):
    def testOutOfRange(self):
        """toRoman should fail with non-integer input"""
        self.assertRaises(roman.InvalidArgument, roman.binsearch, (0.5,1))
    def testSanity1(self):
        """fromRoman(toRoman(n))==n for all n"""
        for integer in range(1, 4000):
            numeral = roman.toRoman(integer)
            result = roman.fromRoman(numeral)
            self.assertEqual(integer, result)

class CaseCheck(unittest.TestCase):
    def testToRomanCase(self):
        """toRoman should always return uppercase"""
        for integer in range(1, 4000):
            numeral = roman.toRoman(integer)
            self.assertEqual(numeral, numeral.upper()) # (1)
    def testFromRomanCase(self):
        """fromRoman should only accept uppercase input"""
        for integer in range(1, 4000):
            numeral = roman.toRoman(integer)
            roman.fromRoman(numeral.upper()) # (2) (3)
            self.assertRaises(roman.InvalidRomanNumeralError,
            roman.fromRoman, numeral.lower())

if __name__ == "__main__":
    unittest.main()
