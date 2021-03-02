"""
Numeric Matrix Processor
author: Arturexp
"""

user_choice = 0


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
        return "\n".join([" ".join(map(str, i)) for i in self.matrix])

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
                    return Matrix([[sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*other)]
                                   for m1_r in self.matrix])
            except MatrixShapeError:
                print("The operation cannot be performed.")
                exit(0)
        else:
            print("The operation cannot be performed.")
            exit(0)


def get_matrix_from_input(choice):
    if choice != 2:
        if Matrix.instances:
            matrix1_exist = 'first'
        else:
            matrix1_exist = 'second'
    else:
        matrix1_exist = ''

    a, b = map(int, input(f'Enter size of {matrix1_exist} matrix: ').split())
    print(f'Enter {matrix1_exist} matrix:')
    return [list(map(lambda x: int(x) if "." not in x else float(x), input().split())) for _ in range(a)]


def constant_value():
    try:
        return int(input('Enter constant: '))
    except ValueError:
        return float(input('Enter constant: '))


def menu():
    print("""1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. Exit""")
    user_choice = int(input("Your choice: "))
    return user_choice


while True:
    user_choice = menu()
    if user_choice == 1:
        matrix1 = Matrix(get_matrix_from_input(user_choice))
        matrix2 = Matrix(get_matrix_from_input(user_choice))
        print('The result is:')
        print(matrix1 + matrix2, '\n')
    elif user_choice == 2:
        matrix = Matrix(get_matrix_from_input(user_choice))
        print('The result is:\n', matrix * constant_value(), '\n')
    elif user_choice == 3:
        matrix1 = Matrix(get_matrix_from_input(user_choice))
        matrix2 = Matrix(get_matrix_from_input(user_choice))
        print('The result is:')
        print(matrix1 * matrix2, '\n')
    elif user_choice == 4:
        print('\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
        choice = int(input("Your choice: "))
        matrix = Matrix(get_matrix_from_input(user_choice))
    else:
        exit(0)
