import toHex as tx
import unittest

class KnownValues(unittest.TestCase): # (1)
    knownValues = ((1,"1"),
                   (3,"3"),
                   (7,"7"),
                   (16,"10"),
                   (32,"20"),
                   (47,"2F"),
                   (48,"30"),
                   (64,"40"),
                   (80,"50"),
                   (256,"100"),
                   (4096,"1000"))
    def testHexKnown(self): # (3)
        """totx should give known result with known input"""
        for num,resK in self.knownValues:
            res = tx.toHex(num)
            self.assertEqual(resK, res)

class NumerCheck(unittest.TestCase):
    def testnotInt(self):
        self.assertRaises(tx.InvArg, tx.toHex, 0.3)
    def testneg(self):
        self.assertRaises(tx.InvArg, tx.toHex, -3)

class CaseCheck(unittest.TestCase):
    def testtoHexCase(self):
        """totx should always return uppercase"""
        for integer in range(1, 16):
            numeral = tx.toHex(integer)
            self.assertEqual(numeral, numeral.upper())

class SanityCheck(unittest.TestCase):
    def testBack(self):
        for integer in range(1,10000):
            hexv = tx.toHex(integer)
            intv = int(hexv, 16)
            self.assertEqual(integer, intv)

if __name__ == "__main__":
    unittest.main()
