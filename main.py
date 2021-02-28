"""
Numeric Matrix Processor
author: Arturexp
"""


class MatrixShapeError(Exception):
    pass


class Matrix:
    instances = True

    def __init__(self, array):
        self.matrix = array
        self.rows = len(array)
        self.columns = len(array[0])
        Matrix.instances = False

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
            print("The operation cannot be performed.")
            exit(0)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[self[i][j] * other for j in range(self.columns)] for i in range(self.rows)])
        elif isinstance(other, Matrix):
            try:
                if self.columns != other.rows:
                    raise MatrixShapeError
                else:
                    return Matrix([[sum(x * y for x, y in zip(m1_row, m2_column))
                                    for m2_column in zip(*self)] for m1_row in other])
            except MatrixShapeError:
                print("The operation cannot be performed.")
                exit(0)
        else:
            print("The operation cannot be performed.")
            exit(0)


def get_matrix_from_input():
    if Matrix.instances:
        matrix1_exist = 'first'
    else:
        matrix1_exist = 'second'

    a, b = map(int, input(f'Enter size of {matrix1_exist} matrix: ').split())
    print(f'Enter {matrix1_exist} matrix:')
    try:
        return [list(map(int, input().split())) for _ in range(a)]
    except ValueError:
        return [list(map(float, input().split())) for _ in range(a)]


def constant_value():
    return float(input())


def menu():
    print("""1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit""")
    user_choice = int(input("Your choice: "))
    return user_choice


#menu()

matrix1 = Matrix(get_matrix_from_input())
matrix2 = Matrix(get_matrix_from_input())


print(matrix1 * matrix2)
