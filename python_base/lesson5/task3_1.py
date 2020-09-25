# Задание 3 вторая часть

translate = {'One': 'Odin', 'Two': 'Dva', 'Three': 'Tri', 'Four': 'Chetire'}
result = []
with open("translate.txt") as file_obj:
    for line in file_obj:
        strings = line.split(" - ")
        print(strings)
        print(translate[strings[0]], "-", strings[1])
        result.append(translate[strings[0]] + " - " + strings[1])
    print(result)
with open("translate_1.txt", "w") as file_obj:
    file_obj.writelines(result)