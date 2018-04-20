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
        a = self.acc / x
        self.setAccumulator(a)
        return a
    def getStatus(self):
        return "Result: " + str(self.getAccumulator())

def main():
    calculator = Calculator(0)
    print(calculator.getStatus())
    calculator.add(1)
    print(calculator.getStatus())
    calculator.subtract(1)
    print(calculator.getStatus())
    calculator.add(2)
    print(calculator.getStatus())
    calculator.multiply(2)
    print(calculator.getStatus())
    calculator.divide(4)
    print(calculator.getStatus())
main()
