"""
Name: SudokuGenerator.py
Author: Chrysostomos Papadopoulos
Date: July 2019

Description: Generates a solved Sudoku Puzzle
"""

from SudokuSolver import no_value, valid_element

from random import shuffle
import copy

def empty_board():
    """
    Creates an empty 9x9 board
    """
    return [[0 for i in range(9)] for j in range(9)]

def generate_board(board):
    """
    Generates a board with random numbers
    """
    numbers = [x for x in range(1,10)]
    for i in range(0,81):
        
        row = i // 9
        col = i % 9

        if board[row][col] == 0:
            shuffle(numbers)                                    #Shuffles the list of numbers
            for number in numbers:
                if valid_element(board, number, (row,col)):     #Checking if the number is valid
                    board[row][col] = number                    #If it is valid add the number from the random list

                    if not no_value(board):                     #Checks for Null Cells
                        return True
                    else:
                        if generate_board(board):               #Calls the same function to the updated board
                            return True
            break
    
    board[row][col]=0  
    return False