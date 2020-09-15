# Задание 4 вторым способом
def my_func(x, y):
    if (x > 0) and (y < 0):
        s = 1
        try:
            for i in range(1, (abs(y) + 1)):
                s *= x
            return 1 / s
        except ZeroDivisionError:
            return


print(my_func(2, -3))
