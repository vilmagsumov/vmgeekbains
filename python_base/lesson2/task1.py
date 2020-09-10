#Задание 1 из домашней работы №2
saved_list = [1, 2, 3, 4]
created_list = [11, "Number", 11.086, saved_list, None]

length_of_list = int(len(created_list))
i = 0
while i < length_of_list:
    print(type(created_list[i]))
    i += 1
