"""
Name: SudokuSolver.py
Author: Chrysostomos Papadopoulos
Date: July 2019

Description: Solves a Sudoku Puzzle
"""

def no_value(board):
    """
    A function which finds the elements with no value
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid_element(board, n, position):
    """
    A function which checks if a specific number is valid for a given cell.
    A number is valid if the number in that cell is not present in the same row,
    column and block.
    """
    #Row
    for i in range(len(board[0])):
        if position[1] != i and board[position[0]][i] == n:
            return False
    
    #Column
    for i in range(len(board)):
        if position[0] != i and board[i][position[1]] == n:
            return False
    
    #Block
    xblock = position[1] // 3
    yblock = position[0] // 3

    #Three boxes(indexing: 0,1,2) with three elements in its axis
    for i in range(yblock*3, yblock*3 + 3):             
        for j in range(xblock * 3, xblock*3 + 3):
            if position != (i,j) and board[i][j] == n:
                return False
    
    return True


def backtrack(board):
    """
    A function where we implement the backtrack algorithm in 
    order to solve the puzzle.
    """
    positions = no_value(board)
    
    #Checks if the board is completed
    if not positions:
        return True
    #Returns the row and column where the board has no value
    else:
        row, col = positions

    for num in range(1,10):                           #Loop through values 1-9
        if valid_element(board, num, (row, col)):     #Check if they are valid solutions
            board[row][col] = num                     #If it is valid, add to the board
            
            if backtrack(board):                      #Call the same function to the updated board 
                return True                         
  
            board[row][col] = 0                       #If we don't find a valid solution we reset the last element
    return False