class Cell:
    def __init__(self, mesh):
        self.mesh = int(mesh)

    def __add__(self, other):
        return Cell(self.mesh + other.mesh)

    def __sub__(self, other):
        return Cell(self.mesh - other.mesh)

    def __mul__(self, other):
        return Cell(self.mesh * other.mesh)

    def __truediv__(self, other):
        return Cell(self.mesh // other.mesh)

    def __str__(self):
        return f'Результат операции {self.mesh * "*"}'



    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.mesh / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.mesh % cells_in_row)}'
        return row

cells1 = Cell(12)
cells2 = Cell(3)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(11))
print(cells1.make_order(1))
print(cells1 / cells2)