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