# Задание 6 из домашней работы №1

first_result = float(input("Введите сколько километров пробежал спортсмен за первый день: "))
necessary_result = float(input("Введите сколько километров должен пробежать спортсмен: "))
day_count = 1;

while necessary_result >= first_result:
    print("%d: день: %.2f" %(day_count, first_result))
    day_count +=1
    first_result = first_result*1.1

print("%d: день: %.2f" %(day_count, first_result))
print("На %d день спортсмен достиг результата - не менее %.2f киломентров" %(day_count, necessary_result))