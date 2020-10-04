# Задание 1 из домашней работы №7

class Matrix:

    def __init__(self, params: list):
        self.params = params

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.params]))

    def __add__(self, other):
        matr1 = [[0 for j in range(len(self.params[0]))] for i in range(len(self.params))]
        for i in range(len(self.params[0])):
            for j in range(len(self.params)):
                matr1[i][j] = self.params[i][j] + other.params[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr1]))


matrix_0 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix_0)
print('\n')
print(matrix_1)
print('\n')
print(matrix_0 + matrix_1)
