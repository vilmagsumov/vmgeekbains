# Задание 3 из домашней работы №7

class Cell:

    def __init__(self, num_of_cells: int):
        self.num_of_cells = num_of_cells

    def __str__(self):
        return str(self.num_of_cells)

    def __add__(self, other):
        return Cell(self.num_of_cells + other.num_of_cells)

    def __sub__(self, other):
        if (self.num_of_cells - other.num_of_cells) > 0:
            return Cell(self.num_of_cells - other.num_of_cells)
        elif (self.num_of_cells - other.num_of_cells) < 0:
            return Cell(other.num_of_cells - self.num_of_cells)
        else:
            print("Клетки одинакового размера, вычитание приведет к уничтожению клетки!")

    def __mul__(self, other):
        return Cell(self.num_of_cells * other.num_of_cells)

    def __truediv__(self, other):
        if (self.num_of_cells == 0) or (other.num_of_cells == 0):
            print("Деление невозможно")
        elif (self.num_of_cells - other.num_of_cells) > 0:
            return Cell(self.num_of_cells // other.num_of_cells)
        elif (self.num_of_cells - other.num_of_cells) < 0:
            return Cell(other.num_of_cells // self.num_of_cells)

    def make_order(self, cells_in_row):
        row = ""
        for i in range(self.num_of_cells // cells_in_row):
            for j in range(cells_in_row):
                row += "*"
            row += "\n"
        for i in range(self.num_of_cells % cells_in_row):
            row += "*"
        return row


cell = Cell(24)
cell2 = Cell(5)

print(cell + cell2)
print(cell - cell2)
print(cell / cell2)
print(cell * cell2)

print(cell.make_order(5))

