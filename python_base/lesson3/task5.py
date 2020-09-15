#Задание 5 из домашней работы №4
def sum ():
    sum = 0
    condition = False
    while condition == False:
        numbers = input('Введите числа или q для выхода: ').split()

        res = 0
        for element in range(len(numbers)):
            if numbers[element] == 'q' or numbers[element] == 'Q':
                condition = True
                break
            else:
                res = res + int(numbers[element])
        sum = sum + res
        print(f'Current sum is {sum}')
    print(f'Your final sum is {sum}')


sum()