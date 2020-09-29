# Задание 4 из домашней работы №6

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость равна {self.speed}")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if (self.speed > 60):
            print("Вы превышаете скорость!")
        else:
            print("Вы едете с разрешенной скорость")


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if (self.speed > 40):
            print("Вы превышаете скорость!")
        else:
            print("Вы едете с разрешенной скоростью")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


townCar = TownCar(55, "Green", "Mazda", False)
townCar.show_speed()
townCar.turn("Left")

workCar = WorkCar(60, "Blue", "Citroen", True)
workCar.show_speed()