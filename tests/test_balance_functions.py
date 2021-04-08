from catan.balance.resource_distribution import measure_resource_distribution
from catan.board.board import Board
from catan.board.known_layouts import perfectly_distributed_layout


def test_measure_resource_distribution():
    # Assert that the measured resource distribution of the perfectly distributed layout is 0
    assert measure_resource_distribution(Board(terrain_types=perfectly_distributed_layout['terrain_types'],
                                               tile_numbers=perfectly_distributed_layout['tile_numbers'])) == 0
