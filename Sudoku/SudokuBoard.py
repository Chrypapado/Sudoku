"""
Name: SudokuBoard.py
Author: Chrysostomos Papadopoulos
Date: July 2019

Description: Prints the grid for the Sudoku puzzle
"""

def your_board():
    """
    A board where anyone can insert their puzzle
    in order to find its solution
    """
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    return board

def print_board(board):
    """
    Creates a 2-D grid with lines seperating each block
    for better visuals.
    """
    for i in range(len(board)):
        if i == 0:
            print("=============================")
        
        if i % 3 == 0 and i != 0:
            print("||- - - - - - - - - - - - -||")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 0:
                print("|| " + str(board[i][j]), end=" ")
            elif j == 8:
                print(str(board[i][j]) + " ||")
            else:
                print(str(board[i][j]) + " ", end="")

        if i == 8:
            print("=============================")