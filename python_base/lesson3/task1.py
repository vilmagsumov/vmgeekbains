#Задание 1 из домашней работы №3

def division(a, b):
    """
    Функция выполняет операцию деления
    :param a: Делимое
    :param b: Делитель
    :return: Результат
    """
    try:
        return a / b
    except ZeroDivisionError:
        return

print(division(1, 2))
print(division(2, 0))