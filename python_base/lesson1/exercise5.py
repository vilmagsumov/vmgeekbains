# Задание 5 из домашней работы №1

# Запрашиваем выручку фирмы
proceeds = float(input("Введите выручку фирмы: "))
# Запрашиваем издержки фирмы
cost = float(input("Введите изжержки фирмы: "))

if proceeds > cost:
    print("Фирма работает с прибылью!")
    profit = (proceeds - cost)/cost
    print("Рентабельность фирмы = %.2f" %(profit))
    num_of_workers = int(input("Введите количество сотрудников: "))
    print("Прибиль фирмы в расчете на одного сотрудника = %.2f" %(profit/num_of_workers))
elif proceeds < cost:
    print("Фирма работает в убыток!")
else:
    print("Фирма работает в ноль!")