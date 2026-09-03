import math

class AreaCalc:
    def calculate(self, length, width=None):
        if width is None:
            area = round(math.pi * length ** 2, 2)
            return area
        else:
            area = length * width
            return area
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
