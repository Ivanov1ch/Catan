from catan.balance.balance_functions import measure_resource_distribution
from catan.board.board import Board
from catan.board.known_layouts import perfectly_distributed_layout


def test_measure_resource_distribution():
    assert measure_resource_distribution(Board(terrain_types=perfectly_distributed_layout['terrain_types'],
                                               tile_numbers=perfectly_distributed_layout['tile_numbers'])) == 0
