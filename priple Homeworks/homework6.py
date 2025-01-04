import os
import shutil

def draw_board(rows, columns):
    """
    Draws a playing board with the specified number of rows and columns.
    
    Parameters:
    rows (int): The number of rows in the playing board.
    columns (int): The number of columns in the playing board.
    
    Returns:
    bool: True if the board is successfully drawn, False if the dimensions exceed the maximum size.
    """
    # Get the terminal size
    terminal_size = shutil.get_terminal_size((80, 20))
    max_width = terminal_size.columns
    max_height = terminal_size.lines
    
    # Calculate the required width and height for the board
    required_width = columns * 4 + 1  
    required_height = rows * 2 + 1  
    
  
    if required_width > max_width or required_height > max_height:
        return False
    
    # Draw the board
    for row in range(rows):
        print(" ---" * columns + " ")
        print("|   " * columns + "|")
    print(" ---" * columns + " ")
    
    return True

# Testing the function
print(draw_board(3, 3))  
print(draw_board(10, 5))  
print(draw_board(50, 100))  
