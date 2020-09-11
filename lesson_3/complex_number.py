class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        result = self * ComplexNumber(other.real, -other.imag)
        ratio = other.real * other.real + other.imag * other.imag
        if ratio != 0:
            result.real /= ratio
            result.imag /= ratio
            return result
        else:
            raise ZeroDivisionError("Error")

    def __str__(self):
        return f"{self.real} + {self.imag}j"


complex_num_1 = ComplexNumber(2, 2)
complex_num_2 = ComplexNumber(1, 4)
complex_num_3 = complex_num_1 + complex_num_2
complex_num_4 = complex_num_1 * complex_num_2
complex_num_5 = complex_num_1 / complex_num_2
print(complex_num_1)
print(complex_num_2)
print(complex_num_3)
print(complex_num_4)
print(complex_num_5)
