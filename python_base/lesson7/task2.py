# Задание 2 из домашней работы №7

class Clothes:

    def __init__(self, name, size, height):
        self.size = size
        self.height = height

    def get_consumption(self):
        if self.name == "palto":
            return self.size / 6.5 + 0.5
        elif self.name == "kostum":
            return 2 * self.height + 0.3
        else:
            return None

    @property
    def get_all_comsumption(self):
        return f"Общий расход ткани равен {self.size / 6.5 + 0.5 + self.height * 2 + 0.3}"


jacket = Clothes("kostum", 4, 10)
coat = Clothes("palto", 10, 5)

print(coat.get_all_comsumption)
print(jacket.get_all_comsumption)