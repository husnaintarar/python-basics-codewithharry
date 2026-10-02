class Calculator:
    def saquare(self, num):
        return num * num

    def cube(self, num):
        return num * num * num

    def square_root(self, num):
        return num ** 0.5

# Usage
calc = Calculator()
print(calc.square_root(9)) # Output: 3.0
print(calc.saquare(4))      # Output: 16
print(calc.cube(3))         # Output: 27