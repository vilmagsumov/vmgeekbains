# Задание 4 из домашней работы №5
# Задание 6 - метод validation


class EquipmentStock:
    pass


class Stock:
    pass


class OfficeEquipment:
    quantity: int
    price: float
    weight: float
    firm_name: str

    def __init__(self, quantity, price, weight, firm_name):
        self.quantity = quantity
        self.price = price
        self.weight = weight
        self.name = firm_name

    def __str__(self):
        return f"Офисное оборудование фирмы {self.name} в количестве {self.quantity} весом {self.weight} ценой {self.price}."

    @staticmethod
    def validation(quantity, price, weight):
        try:
            quantity = int(quantity)
            price = float(price)
            weight = float(weight)
            return f"Количество: {quantity}\nЦена: {price}\nВес: {weight}"
        except ValueError:
            print("Введены нерорректные данные!")
            inpt = input("Введите y для повторного ввода данных")
            if inpt == "y":
                return OfficeEquipment.validation()
            else:
                return f"Validation error"


class Printer(OfficeEquipment):
    print_format: str
    lists_in_minute: int

    def __init__(self, print_format, lists_in_minute):
        self.print_format = print_format
        self.lists_in_minute = lists_in_minute


class Scanner(OfficeEquipment):
    scan_format:str

    def __init(self, scan_format):
        self.scan_format = scan_format


class Copier(OfficeEquipment):
    copy_format: str

    def __init__(self, copy_format):
        self.copy_format = copy_format




print(OfficeEquipment.validation(1, 1531, 541))

equipment = OfficeEquipment(1, 11, 15.54, "Xerox")
print(equipment)
print(equipment.validation(equipment.quantity, equipment.price, equipment.weight))