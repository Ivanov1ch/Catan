import random

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
