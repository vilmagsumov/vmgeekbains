#Задание2 из домашней рабоыт №3
def user_data(name, surname, born_year, city, email, tel_number):
    """Выводит данные о пользователе, принимает именнованные аргументы"""
    print(f"{name}, {surname}, {born_year}, {city}, {email}, {tel_number}")

user_data(name="John", city="New York", email="name@name.com", surname="Smith", tel_number="88988888888", born_year="1978")