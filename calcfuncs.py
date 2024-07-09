import math

class Calc:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y;

    def divide(self, x, y):
        return x / y;

    def multiply(self, x, y):
        return x * y;

    def sin(self, x):
        xInRadians = x * math.pi/180
        return xInRadians - pow(xInRadians, 3)/math.factorial(3) + pow(xInRadians, 5)/math.factorial(5) - pow(xInRadians, 7)/math.factorial(7) + pow(xInRadians, 9)/math.factorial(9) - pow(xInRadians, 11)/math.factorial(11)
    def cos(self, x):
        xInRadians = x * math.pi/180
        return 1 - math.pow(xInRadians, 2)/math.factorial(2) + math.pow(xInRadians, 4)/math.factorial(4) - math.pow(xInRadians, 6)/math.factorial(6) + math.pow(xInRadians, 8)/math.factorial(8)
