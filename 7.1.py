
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([f"{itm:02}" for itm in line]) for line in self.matrix)

    def __add__(self, other):
        try:
            m = [[int(self.matrix[line][itm]) + int(other.matrix[line][itm]) for itm in range(len(self.matrix[line]))]
                 for line in range(len(self.matrix))]
            return Matrix(m)
        except IndexError:
            return f"Проблема разноразмерности матриц"

m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_2 = [[5, 8, 2], [4, 7, 1], [6, 9, 3]]

matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)
sum_m = matrix_1 + matrix_2

print(f'Matrix 1\n{matrix_1}\n{"*" * 7}')
print(f'Matrix 2\n{matrix_2}\n{"*" * 7}')
print(f'Sum\n{sum_m}')

