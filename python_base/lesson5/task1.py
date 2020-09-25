#Задание 1 из домашеней работы №5

with open("text_file.txt", "w") as file_obj:
    while True:
        text_str = input("Введите строку данных: ")
        if text_str == "":
            break
        else:
            print(text_str, file=file_obj)