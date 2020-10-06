# Задание 2 из домашней работы №8

class CorrectZeroDivision(Exception):
    def __init__(self, inp_divident, inp_divider):
        self.divident = inp_divident
        self.divider = inp_divider

    @staticmethod
    def division(inp_divident, inp_divider):
        try:
            result = inp_divident / inp_divider
        except ZeroDivisionError:
            result = "Вы пытаетесь разделить число на 0"
        return result


first = float(input("Введите делимое: "))
second = float(input("Введитель делитель: "))

print(CorrectZeroDivision.division(first, second))
