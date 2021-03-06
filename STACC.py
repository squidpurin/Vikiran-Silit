import unittest
class OutOfRangeError(Exception):
    pass

class Stack:
    def __init__(self):
        self.elem = []
    def push(self, x):
        self.elem.append(x)
    def isEmpty(self):
        if self.size() == 0:
            return True
        return False
    def size(self):
        return len(self.elem)
    def peek(self):
        if(self.size() == 0):
            raise OutOfRangeError
        if self.size()!= 0:
            return self.elem[-1]
        return None
    def pop(self):
        if self.size() == 0:
            raise OutOfRangeError
        x = self.elem[-1]
        del self.elem[-1]
        return x
    
class StackTest(unittest.TestCase):
    def setUp(self):
        self.s = Stack()
    def testNewStack(self): # (1)
        self.assertTrue(self.s.isEmpty())
        self.assertEqual(self.s.size(), 0)
    def testPushes(self): # (2)
        nPushes = 6
        for i in range(nPushes):
            self.s.push("item")
        self.assertFalse(self.s.isEmpty())
        self.assertEqual(self.s.size(), nPushes)
    def testPushPop(self): # (3)
        size = self.s.size()
        item = "Python"
        self.s.push(item)
        self.assertEqual(self.s.pop(), item)
        self.assertEqual(self.s.size(), size)
    def testPushPeek(self): # (4)
        item = "Python"
        self.s.push(item)
        size = self.s.size()
        self.s.peek()
        self.assertEqual(self.s.size(), size)
    def testNPop(self): # (5)
        size = self.s.size()
        for i in range(size):
            self.s.pop()
        self.assertTrue(self.s.isEmpty())
    def testPopEmptyStack(self): #6
        self.assertRaises(OutOfRangeError, self.s.pop)
    def testPeekEmptyStack(self): #7
        self.assertRaises(OutOfRangeError, self.s.peek)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(StackTest))
    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(StackTest("testNewStack"))
    suite.addTest(StackTest("testPushes"))
    return suite

unittest.TextTestRunner().run(suite())
#unittest.TextTestRunner(verbosity=2).run(suite2())
