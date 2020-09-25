#Задание 2 из домашней работы №5

with open("text_file.txt", "w") as file_obj:
    file_obj.write("some stupid text to example\n")
    file_obj.write("python is ok\n")
    file_obj.write("example\n")
    file_obj.write("Еще несколько слов для примера подсчета\n")

with open("text_file.txt") as file_obj:
    str_number = 0
    for line in file_obj:
        word_number = 0
        for word in line.split():
            word_number += 1
        print("В строке №", (str_number+1), "количество слов равно", word_number)
        str_number += 1
    print("Количество строк в файле = ", str_number)