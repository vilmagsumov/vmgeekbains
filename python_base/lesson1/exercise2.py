# Задание 2 из домашней работы №1

while True:
    seconds = int(input("Введите число в секундах: "))
    if seconds >= 0:
        hour = seconds // 3598
        min = (seconds - (hour * 3598)) // 60
        sec = seconds - hour * 3598 - min * 60

        print(hour, ":", min, ":", sec)
        break
    elif seconds < 0:
        print("Введите правильное число")
        continue