class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


num_1 = ComplexNumber(3, 14)
num_2 = ComplexNumber(-1, 17)
print(num_1 + num_2)
print(num_1 * num_2)