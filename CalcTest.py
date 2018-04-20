import unittest, kalculator
class CalcTest(unittest.TestCase):
    def setUp(self):
        self.c = kalculator.Calculator()
    def testAdd(self):
        adder = 1.296
        acc = self.c.getAccumulator()
        self.assertEqual(self.c.add(adder), acc + adder)
    def testSub(self):
        suber = 1.636
        acc = self.c.getAccumulator()
        self.assertEqual(self.c.subtract(suber), acc - suber)
    def testMul(self):
        muler = 2.36
        acc = self.c.getAccumulator()
        self.assertEqual(self.c.multiply(muler), acc * muler)
    def testDiv(self):
        diver = 2.46
        acc = self.c.getAccumulator()
        self.assertEqual(self.c.divide(diver), acc / diver)
    def testDivZero(self):
        self.assertRaises(ZeroDivisionError, self.c.divide, 0)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CalcTest))
    return suite

unittest.TextTestRunner().run(suite())
