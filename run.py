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


def create_grid():
    """
    Create a 5x5 grid filled with dots and global variables for grid size
    """
    global grid
    global grid_size

    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
    Functions for validating and placing ships on the grid
    """
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


def create_grid():
    """
    Randomly place ships on the grid during grid creation
    """
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    num_of_ships_placed = 0
    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, grid_size - 1)
        random_col = random.randint(0, grid_size - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1


def print_grid():
    """
    Display only hits and misses, conceal ship positions
    """
    global grid
    global alphabet

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "X" or grid[row][col] == "#":
                print(grid[row][col], end=" ")
            else:
                print(".", end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")



def accept_valid_bullet_placement():
    """
    Functions for accepting valid bullet placement from the user
    """
    global alphabet
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-E) and column (0-4) such as B3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as B3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-E) for row and (0-4) for column")
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter letter (A-E) for row and (0-4) for column")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter letter (A-E) for row and (0-4) for column")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_placement = True

    return row, col


def shoot_bullet():
    """
    Update the grid based on user's bullet placement
    """
    global grid
    global num_of_ships_sunk
    global bullets_left

    row, col = accept_valid_bullet_placement()
    print("")

    if grid[row][col] == ".":
        print("You missed, no ship was shot")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        num_of_ships_sunk += 1
        print("A ship was completely sunk!")

    bullets_left -= 1


def check_for_ship_sunk(row, col):
    """
    Determine if a ship is completely sunk after a bullet hit
    """
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True


def check_for_game_over():
    """
    Check for game over based on ships sunk or bullets remaining
    """
    global num_of_ships_sunk
    global num_of_ships
    global bullets_left
    global game_over

    if num_of_ships == num_of_ships_sunk:
        print("Congrats you won!")
        game_over = True
    elif bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        game_over = True


# ASCII art 
def print_ascii_art():
    print("                                     # #  ( )")
    print("                                  ___#_#___|__")
    print("                              _  |____________|  _")
    print("                       _=====| | |            | | |==== _")
    print("                 =====| |.---------------------------. | |====")
    print("   <--------------------'   .  .  .  .  .  .  .  .   '--------------/")
    print("     \\                                                             /")
    print("      \\_______________________________________________WWS_________/")
    print("  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    print("   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")

def main():
    """
    Complete the main loop and handle game over scenarios
    """
    global game_over

    print_ascii_art()
    print("\n-----Welcome, Admiral! Prepare for the ultimate naval showdown.-----\n")

    create_grid()

    while not game_over:
        print_grid()
        print(f"Number of ships remaining: {num_of_ships - num_of_ships_sunk}")
        print(f"Number of bullets left: {bullets_left}")
        shoot_bullet()
        check_for_game_over()


if __name__ == '__main__':
    main()
