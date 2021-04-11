import random

from catan.balance.calculate_balance import calculate_balance
from catan.board.beginner_layout import beginner_layout
from catan.board.board import Board


def generate_random_board():
    # Uses random.shuffle() on each required component of the beginner_layout (the terrain_types and tile_numbers arrays
    # ) to build and return a randomized board. We shuffle copies of the arrays to leave beginner_layout unaffected
    terrain_types = beginner_layout['terrain_types'].copy()
    tile_numbers = beginner_layout['tile_numbers'].copy()

    random.shuffle(terrain_types)
    random.shuffle(tile_numbers)

    return Board(terrain_types=terrain_types, tile_numbers=tile_numbers)


# Generates num_random boards and returns the one that results in the LOWEST catan.balance.calculate_balance score,
# followed by its generated score
def generate_balanced_board(num_random):
    return find_best_board(num_random, True)


# Generates num_random boards and returns the one that results in the HIGHEST catan.balance.calculate_balance score,
# # followed by its generated score
def generate_unbalanced_board(num_random):
    return find_best_board(num_random, False)


# The helper function that contains the common code shared by generate_balanced_board and generate_unbalanced_board:
# This function calls generate_random_board num_random times, and seeks the Board with the maximum or the minimum
# catan.balance.calculate_balance return value, as determined by is_seeking_balanced (if it is not seeking the most
# balanced board, it seeks for the least balanced board)
def find_best_board(num_random, is_seeking_balanced):
    # The current best (either highest or lowest, as determined by is_seeking_balanced) returned score
    current_best_score = 1 if is_seeking_balanced else 0
    # The Board that resulted in the current_best_score - defaults to the beginner layout so that a valid board will
    # always be returned, regardless of the value of num_random
    current_best_board = Board(terrain_types=beginner_layout['terrain_types'],
                               tile_numbers=beginner_layout['tile_numbers'])

    for board_num in range(num_random if num_random > 0 else 0):
        board_to_test = generate_random_board()
        balance_score = calculate_balance(board_to_test)

        # Update the current_best_score and current_best board accordingly, based on is_seeking_balanced
        if (is_seeking_balanced and balance_score <= current_best_score) or (
                not is_seeking_balanced and balance_score >= current_best_score):
            current_best_board = board_to_test
            current_best_score = balance_score

    return current_best_board, current_best_score
