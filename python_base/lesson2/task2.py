#Задание 2 из домашней работы №2
inp_list = []
while True:
    new_elem = input("Введите новое значение: ")
    if new_elem == "stop":
        break
    else:
        inp_list.append(new_elem)
print("Исходный список: ", inp_list)
length_of_list = int(len(inp_list))
k = 0
if length_of_list % 2 == 0:
    while k < length_of_list:
        tmp = inp_list[k]
        inp_list[k] = inp_list[k+1]
        inp_list[k+1] = tmp
        k += 2
elif length_of_list % 2 == 1:
    while k < (length_of_list - 1):
        tmp = inp_list[k]
        inp_list[k] = inp_list[k+1]
        inp_list[k+1] = tmp
        k += 2
print("Новый список", inp_list)

