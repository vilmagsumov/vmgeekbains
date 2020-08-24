# Задание 3 из домашней работы №1

while True:
    n = input("Введите положительное число: ")
    if int(n) > 0:
        nn = int(n + n)
        nnn = int(n + n + n)

        print(int(n) + int(nn) + int(nnn))
        break
    else:
        print("Введи правильное число!")
        continue
