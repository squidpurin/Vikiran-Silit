import unittest
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
        if self.size()!= 0:
            return self.elem[-1]
        return None
    def pop(self):
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

if __name__ == "__main__":
    unittest.main(verbosity = 2)

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
unittest.TextTestRunner(verbosity=2).run(suite2())
