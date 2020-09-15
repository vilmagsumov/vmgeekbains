#Задание 3 из домащней работы №3
def my_func(a, b, c):
    """
    Возращает сумму двух наибольших аргументов
    :param a: Аргумент 1
    :param b: Аргумент 2
    :param c: Аргумент 3
    :return: Сумма двух наибольших
    """
    s = 0
    if (a > b) and (b > c):
        s = a + b
    elif (a > c) and (c > b):
        s = a + c
    elif (b > c) and (c > a):
        s = b + c
    elif (c > a) and (a > b):
        s = c + a
    elif (c > b) and (b > a):
        s = b + c
    else:
        s = a + b

    return s

print(my_func(1, 2, 3))
print(my_func(1, 3, 2))
print((my_func(2, 3, 1)))
print(my_func(3, 1, 2))
print(my_func(3, 2, 1,))
print(my_func(2, 1, 3))