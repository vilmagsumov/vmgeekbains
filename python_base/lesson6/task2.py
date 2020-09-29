# Задание 2 из домашней работы №6

class Road:
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def mass(self, unit_mass, thickness):
        return self.__length * self.__width * unit_mass * thickness


Road = Road(100, 20)
print(Road.mass(2, 3))
