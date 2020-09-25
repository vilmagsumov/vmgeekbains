# Задание №3 из домашней работы №5

with open("text_file.txt") as file_obj:
    salary_sum = 0
    counter = 0
    for line in file_obj:
        surname, salary = line.split()
        salary = int(salary)
        if ( salary < 20000 ):
            print(surname)
        salary_sum += salary
        counter += 1
    print("Средний доход сотрудников равен:", salary_sum/counter)