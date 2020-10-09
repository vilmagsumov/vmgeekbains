# Задание 7 из домашней работы №8

class Complex:
    real: float
    imaginary: float

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} {self.imaginary}i"

    def __add__(self, other):
        if ( self.imaginary + other.imaginary ) > 0:
            return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
        else:
            return f"{self.real + other.real} {self.imaginary + other.imaginary}i"

    def __mul__(self, other):
        if (self.real * other.imaginary + other.real * self.imaginary) > 0:
            return f"{self.real * other.real - self.imaginary * other.imaginary} + {self.real * other.imaginary + other.real * self.imaginary}"
        else:
            return f"{self.real * other.real - self.imaginary * other.imaginary} {self.real * other.imaginary + other.real * self.imaginary}i"


a = Complex(1.22, -5)
b = Complex(5, 6)
print(a)
print(b)
print(a + b)
print(a * b)
