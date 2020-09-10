#Задание 4 из домашней работы №2
inp_str = input("Введите строку из нескольких слов, разделенных пробелами: ")
words = inp_str.split()
for i in range(len(words)-1):
    if len(words[i]) > 10:
        print(words[i][0:10])
        i += 1
    else:
        print(words[i])
        i += 1