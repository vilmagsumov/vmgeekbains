# Задание 3 из домашней работы №8

class IsNumber(Exception):

    def __init__(self, *args):
        self.numbers = []

    def controlNumberList(self):
        while True:
            try:
                input_val = input("Введите новый элемент списка: ")
                self.numbers.append(float(input_val))
            except ValueError:
                if input_val == "stop":
                    print("Ввод завершен!")
                    break
                else:
                    print("Пожалуйста введите число!")
                    continue
        return self.numbers


numberList = IsNumber(1)
print(numberList.controlNumberList())