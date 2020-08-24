# Задание 4 из домашней работы № 1

while True:
    number = input("Введите целое положительное число: ")
    if (float(number) % 1 == 0.0) and (int(number) > 0):
        number = int(number)
        max_number = number % 10
        while number > 0:
            if number % 10 > max_number:
                max_number = number % 10
            number = number // 10
        break
    else:
        print("Введите правильное число!")
        continue
print("Самая большая цифра числа = ", max_number)
