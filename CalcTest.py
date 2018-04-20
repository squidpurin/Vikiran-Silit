import unittest, kalculator
class CalcTest(unittest.TestCase):
    def setUp(self):
        self.c = kalculator.Calculator()
    def testInit(self): #check initial accumulator if it is 0.0
        self.assertEqual(self.c.getAccumulator(), 0)
    def testAdd(self): #test if adder adds correctly
        adder = 1.296
        acc = self.c.getAccumulator()
        self.assertEqual(self.c.add(adder), acc + adder)
    def testSub(self): #test if subtracter subtracts correctly
        suber = 1.636
        acc = self.c.getAccumulator()
        self.assertEqual(self.c.subtract(suber), acc - suber)
    def testMul(self): #test if multiplier multiplies correctly
        muler = 2.36
        acc = self.c.getAccumulator()
        self.assertEqual(self.c.multiply(muler), acc * muler)
    def testDiv(self): #test if divider divides correctly
        diver = 2.46
        acc = self.c.getAccumulator()
        self.assertEqual(self.c.divide(diver), acc / diver)
    def testDivZero(self): #test if divider is not zero
        self.assertRaises(ZeroDivisionError, self.c.divide, 0)
    def testDataType(self): #check data type of input whether it is numeric
        self.assertRaises(TypeError, self.c.add, [1])
        self.assertRaises(TypeError, self.c.subtract, [1])
        self.assertRaises(TypeError, self.c.multiply, [1])
        self.assertRaises(TypeError, self.c.divide, [1])
    def testSetGet(self):
        x = 5
        self.c.setAccumulator(x)
        y = self.c.getAccumulator()
        self.assertEqual(x, y)
    def testStatus(self):
        self.assertEqual(self.c.getStatus(), "Result: " + str(self.c.getAccumulator()))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CalcTest))
    return suite

unittest.TextTestRunner().run(suite())
