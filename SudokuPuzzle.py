"""
Name: SudokuGenerator.py
Author: Chrysostomos Papadopoulos
Date: July 2019

Description: Creates a Sudoku Puzzle
"""

from SudokuGenerator import generate_board, empty_board
from SudokuSolver import valid_element
from SudokuBoard import print_board

from random import shuffle

def numbers(board):
    """
    A function where all the cells positions 
    are saved in a list
    """
    numbers_position = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                numbers_position.append((i,j))
    
    return numbers_position

def possible_values(board, position):
    """
    A function which checks how many solutions
    exist for a given cell
    """
    count = 0
    temp = board[position[0]][position[1]]
    board[position[0]][position[1]] = 0
    for n in range(1,10):
        if valid_element(board, n, position):
            count += 1
    board[position[0]][position[1]] = temp
    return count

def puzzle(board, rounds = 81):
    """
    A function where the puzzle is created by removing cells
    """
    numbers_position = numbers(board)
    shuffle(numbers_position)

    for n in numbers_position:
        
        if possible_values(board, n) == 1:    
            board[n[0]][n[1]] = 0
            rounds -= 1

        if rounds == 0:
            break