# Задание 5 из домашней работы №2
rating = [7, 5, 4, 3, 3, 2]
while True:
    new_elem = int(input("Введите новое значение: "))
    rating.append(new_elem)
    rating.sort(reverse=True)
    print(rating)