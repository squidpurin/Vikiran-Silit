import toHex as roman
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
        """toRoman should give known result with known input"""
        for num,resK in self.knownValues:
            res = roman.toHex(num)
            self.assertEqual(resK, res)
