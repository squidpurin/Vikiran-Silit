import math
import unittest
from precision import *
from Circle import *
class CircleTest(unittest.TestCase):
    def setUp(self):
        self.c = Circle(0,0,10)
    def testRadAreaRad(self): # Sanity check to see if reverse-calculated radius from area is the same as original radius
        rad = self.c.radius
        area = self.c.getArea()
        dRad = precision(math.sqrt(area / math.pi), 6) 
        self.assertEqual(rad, dRad)
    def testRedPeriRad(self): # Same as above but with radius from perimeter
        rad = self.c.radius
        peri = self.c.getPerimeter()
        dRad = precision(peri / (2 * math.pi), 6)
        self.assertEqual(rad, dRad)
    def testPosRad(self): # Test to see that radius should be positive
        rad = self.c.radius
        checkPos = rad >= 0
        self.assertTrue(checkPos)
    def testDataType(self): # Test for numeric datatype
        self.assertRaises(TypeError,Circle, [1], [2], [3])
        self.assertRaises(TypeError,self.c.move, [1,2,3], [3])

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CircleTest))
    return suite

unittest.TextTestRunner().run(suite())
