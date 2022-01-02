class Cell:
    def __init__(self, nums):
        self.nums = nums
    def make_order(self, rows):
        return '\n'.join(["☻" * rows for _ in range(self.nums // rows)]) + '\n' + "☻" * (self.nums % rows)
    def __str__(self):
        return f'{self.nums}'
    def __add__(self, other):
        print('Sum of cells is: ')
        return Cell(self.nums + other.nums)
    def __sub__(self, other):
        print('Subtration of cell is: ')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Отрицательное число получиться не может'
    def __mul__(self, other):
        print('Multyply of cell is: ')
        return Cell(self.nums * other.nums)
    def __floordiv__(self, other):
        print('Division of cell is: ')
        return Cell(self.nums // other.nums)

cell_1 = Cell(12)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(5))

