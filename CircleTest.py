import math
import unittest
from precision import *
from Circle import *

class CircleTest(unittest.TestCase):
    def setUp(self):
        self.c = Circle(0,0,10)
    def testRadAreaRad(self):
        rad = self.c.radius
        area = self.c.getArea()
        dRad = precision(math.sqrt(area / math.pi), 6)
        self.assertEqual(rad, dRad)
    def testRedPeriRad(self):
        rad = self.c.radius
        peri = self.c.getPerimeter()
        dRad = precision(peri / (2 * math.pi), 6)
        self.assertEqual(rad, dRad)
    def testPosRad(self):
        rad = self.c.radius
        checkPos = rad >= 0
        self.assertTrue(checkPos)
