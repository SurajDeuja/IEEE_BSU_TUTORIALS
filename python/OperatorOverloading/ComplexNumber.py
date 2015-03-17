class Complex:
    def __init__(self, num):
        self.i = num[0]
        self.j = num[1]

    def __str__(self):
        return '({0} + {1}j)'.format(self.i, self.j)

    def __add__(self, other):
        return Complex([self.i + other.i, self.j + other.j])

    def __sub__(self, other):
        return Complex([self.i - other.i, self.j - other.j])

num1 = Complex([1, 2])
num2 = Complex([3, 4])

print num1, "+", num2, "=", num1 + num2
print num1, "-", num2, "=", num1 - num2