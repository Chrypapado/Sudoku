from Sudoku.SudokuBoard import print_board
from Sudoku.SudokuGenerator import generate_board, empty_board
from Sudoku.SudokuPuzzle import puzzle

#Creates an empty board
board = empty_board()

#Generates a fully solved Sudoku puzzle
generate_board(board)

#Removes cells in order to create the puzzle (with a unique solution)
puzzle(board, rounds = 60)

#Prints the grid
print_board(board)