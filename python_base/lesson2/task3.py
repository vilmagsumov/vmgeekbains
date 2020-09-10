#Задание 3 из домашней работы №2
month = int(input("Введите номер месяца: "))
summer_mounts = [6, 7, 8]
autumm_mounts = [9, 10, 11]
winter_mounts = [12, 1, 2]
spring_mounts = [3, 4, 5]

year_time = dict(summer=summer_mounts,
                 autumm=autumm_mounts,
                 winter=winter_mounts,
                 spring=spring_mounts)
for key in year_time.keys():
    if month in year_time[key]:
        print(key)
