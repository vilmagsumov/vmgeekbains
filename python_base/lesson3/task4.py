# Задание 4 из домашней работы №3
def my_func(x, y):
    """
    ВОзведение числа в степень
    :param x: действительное положительное число
    :param y: степень - целое отрицательное число
    :return: результат
    """
    if (x > 0) and (y < 0):
        return x ** (y)
    else:
        return

print(my_func(2, -3))
