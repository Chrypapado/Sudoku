import sys
import fileinput

from Sudoku.SudokuBoard import print_board
from Sudoku.SudokuSolver import backtrack

board = []

for row in fileinput.input():
    board.append(row.strip().split(' '))

for i in range(len(board)):
    for j in range(len(board)):
        board[i][j] = int(board[i][j])

backtrack(board)
print_board(board)

