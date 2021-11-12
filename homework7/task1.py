import random as rnd

class Matrix:
    def __init__(self, matrix):
        self.__matrix = matrix
        self.__row_num = len(matrix)
        self.__col_num = len(matrix[0])

    def __str__(self):
        res_str = ""
        for row in self.__matrix:
            res_str += " ".join([str(num) for num in row]) + "\n"
        return res_str

    def __add__(self, other):
        res_matrix = [[]]
        other_row_num = len(other.__matrix)
        other_col_num = len(other.__matrix[0])
        if self.__row_num == other_row_num and self.__col_num == other_col_num:
            res_matrix = [[self.__matrix[j][i] + other.__matrix[j][i] for i in range(self.__col_num)] for j in range(self.__row_num)]
        else:
            print("Operation is not possible for matrices of different sizes!")
        return Matrix(res_matrix)


numRows = int(input("Input number of rows: "))
numCols = int(input("Input number of columns: "))
list_of_lists = [[rnd.randint(0, 20) for _ in range(numCols)] for x in range(numRows)]
matr = Matrix(list_of_lists)
print(f'Initial matrix is: \n{matr}')
another_list_of_lists = [[rnd.randint(0, 20) for _ in range(numCols)] for x in range(numRows)]
another_matr = Matrix(another_list_of_lists)
print(f'Another matrix is: \n{another_matr}')
print(f'Result matrix: \n{matr + another_matr}')