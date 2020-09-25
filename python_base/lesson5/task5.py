# Задание 5 из домашней работы №5

import json

lesson = []
lessons_dict = {}

with open("lessons.txt") as file:
    for line in file:
        lesson = line.split()
        print(lesson)
        summ_of_lessons = 0
        for item_sum in lesson:
            try:
                item_sum = int(item_sum)
                summ_of_lessons += item_sum
            except ValueError:
                continue
        lessons_dict[lesson[0]] = summ_of_lessons
    print(lessons_dict)