import random
import time

"""
    -------BATTLESHIPS-------
    How it will work:
    1. A 5X5 grid will have 3 ships of variable length randomly placed about
    2. You will have 10 bullets to take down the ships that are placed down
    3. You can choose a row and column such as B3 to indicate where to shoot
    4. For every shot that hits or misses it will show up in the grid
    5. A ship cannot be placed diagonally, so if a shot hits the rest of
        the ship is in one of 4 directions, left, right, up, and down
    6. If all ships are sunk before using up all bullets, you win
        else, you lose

    Legend:
    1. "." = water or empty space
    2. "O" = part of ship
    3. "X" = part of ship that was hit with bullet
    4. "#" = shot in the water, a miss because it hit no ship
"""

# Global variable for grid
grid = [[]]
# Global variable for grid size
grid_size = 5
# Global variable for number of ships to place
num_of_ships = 3
# Global variable for bullets left
bullets_left = 10
# Global variable for game over
game_over = False
# Global variable for number of ships sunk
num_of_ships_sunk = 0
# Global variable for ship positions
ship_positions = [[]]
# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMN"

# Create a 5x5 grid filled with dots and global variables for grid size
def create_grid():
    global grid
    global grid_size

    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

Functions for validating and placing ships on the grid
def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid

def try_to_place_ship_on_grid(row, col, direction, length):
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)
