class Cell:
    def __init__(self, count):
        self.__count = count

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        diff = self.count - other.count
        if diff > 0:
            return Cell(diff)
        else:
            print("Operation is impossible because difference is negative...")
            return None

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(int(self.count / other.count))

    def __str__(self):
        return f'{self.count} cells'

    def make_order(self, cells_in_row):
        full_rows = self.count // cells_in_row
        mod_row = self.count % cells_in_row
        str_full_rows = "\n".join(['*' * cells_in_row for _ in range(full_rows)])
        if mod_row != 0 and str_full_rows:
            str_full_rows += "\n"
        str_full_rows += '*' * mod_row
        return str_full_rows


cell1 = Cell(int(input("Input 1st count of cells: ")))
cell2 = Cell(int(input("Input 2st count of cells: ")))
cell3 = Cell(int(input("Input 3rd count of cells: ")))
cell4 = Cell(int(input("Input 4th count of cells: ")))

print(f'Cell 1 + Cell 2 = {cell1 + cell2}')
print(f'Cell 2 - Cell 3 = {cell2 - cell3}')
print(f'Cell 3 * Cell 4 = {cell3 * cell4}')
print(f'Cell 4 / Cell 1 = {cell4 / cell1}')

cells_in_row = int(input("Input cells in row: "))
print(f'Make order for Cell 1: \n{cell1.make_order(cells_in_row)}')
print(f'Make order for Cell 2: \n{cell2.make_order(cells_in_row)}')
print(f'Make order for Cell 3: \n{cell3.make_order(cells_in_row)}')
print(f'Make order for Cell 4: \n{cell4.make_order(cells_in_row)}')