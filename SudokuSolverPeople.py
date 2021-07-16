import numpy as np


from Sudoku import Sudoku


class SudokuSolverPeople(Sudoku):
    def __init__(self, sudoku: Sudoku):
        super().__init__()
        self.sudoku = sudoku

    # Зполняем поле с координатами (i; j) и значением number
    def set_number(self, i, j, number):
        pass

    def save(self):
        pass

    def upload(self):
        pass
