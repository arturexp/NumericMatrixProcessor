"""
Numeric Matrix Processor
author: Arturexp
"""


class MatrixShapeError(Exception):
    pass


class Matrix:
    def __init__(self, array):
        self.matrix = array
        self.rows = len(array)
        self.columns = len(array[0])

    @property
    def shape(self):
        return self.rows, self.columns

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        return "\n".join([" ".join(map(str, i)) for i in self.matrix])

    def __repr__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.matrix])

    def __add__(self, other):
        try:
            if self.shape != other.shape:
                raise MatrixShapeError
            else:
                return Matrix([[self[i][j] + other[i][j] for j in range(self.columns)] for i in range(self.rows)])
        except MatrixShapeError:
            print("ERROR")
            exit(0)


def get_matrix_from_input():
    a, b = map(int, input().split())
    return [list(map(int, input().split())) for _ in range(a)]


matrix1 = Matrix(get_matrix_from_input())
matrix2 = Matrix(get_matrix_from_input())

print(matrix1 + matrix2)
