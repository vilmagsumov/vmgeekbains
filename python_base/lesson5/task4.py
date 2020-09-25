# Задание 4 из домашней работы №5

import random

# Заполняем файл произвольными числами в интервале от 0 до 100
with open("numbers.txt", "w") as numbers_file:
    for i in range(0, 20):
        numbers_file.write(str(random.randint(0, 100)))
        numbers_file.write(" ")

with open("numbers.txt") as file:
    summa = 0
    for i in file.read().split():
        print(i)
        summa += int(i)
    print("Сумма равна:", summa)
