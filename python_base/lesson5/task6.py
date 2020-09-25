# Задание 6 из домашней работы №5

import json

profit = {}
average = {"average_profit": 0}
summ = 0

with open("firms.txt") as file_obj:
    i = 0
    for line in file_obj:
        firm_name, own_type, proceeds, costs = line.split()
        profit[firm_name] = int(proceeds) - int(costs)
        if ( profit[firm_name] > 0 ):
            summ += profit[firm_name]
            i += 1
        average["average_profit"] = summ/i
    print(profit)
    print(average)
    res = []
    res.append(profit)
    res.append(average)
with open("json_firms.txt", "w") as file:
    json.dump(res, file)