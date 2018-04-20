class Calculator:
    def __init__(self,acc = 0):
        self.acc = acc
    def setAccumulator(self, a):
        self.acc = a
    def getAccumulator(self):
        return self.acc
    def add(self,x):
        a = self.acc + x
        self.setAccumulator(a)
        return a
    def subtract(self,x):
        a = self.acc - x
        self.setAccumulator(a)
        return a
    def multiply(self,x):
        a = self.acc * x
        self.setAccumulator(a)
        return a
    def divide(self,x):
        if x == 0:
            raise ZeroDivisionError
        a = self.acc / x
        self.setAccumulator(a)
        return a
    def getStatus(self):
        return "Result: " + str(self.getAccumulator())
