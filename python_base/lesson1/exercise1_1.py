# Задание 1 из домашней работы №1

while True:
    new_password_0 = input("Введите новый пароль: ")
    new_password_1 = input("Повторите пароль")
    if new_password_0 == new_password_1:
        password = new_password_0
        print("Ваш пароль успешно изменен на ", password)
        break
    else:
        print("Пароли не совпадают, введите пароль повторно")
        continue


