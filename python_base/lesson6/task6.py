# Задание 6 из домашней работы №6

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"1 Запуск отрисовки {self.title}")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"2 Запуск отрисовки {self.title}")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"3 Запуск отрисовки {self.title}")


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"4 Запуск отрисовки {self.title}")


stationery = Stationery("канцелярка")
stationery.draw()

pen = Pen("Ручка")
pen.draw()

pencil = Pencil("карандаш")
pencil.draw()

handle = Handle("маркер")
handle.draw()
