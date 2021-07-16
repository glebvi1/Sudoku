from Sudoku import Sudoku
from SudokuSolver import SudokuSolver

field = Sudoku().generate_field()
SudokuSolver(field).solve().beauty_print()
print()
field.beauty_print()

