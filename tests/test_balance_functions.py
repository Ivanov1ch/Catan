from catan.balance.probability_clustering import measure_probability_clustering
from catan.balance.probability_distribution_on_board import measure_probability_distribution_on_board
from catan.balance.probability_distribution_per_resource import measure_probability_distribution_per_resources
from catan.balance.resource_clustering import measure_resource_clustering
from catan.balance.resource_distribution import measure_resource_distribution
from catan.board.board import Board
from tests.known_layouts import *


def test_measure_resource_distribution():
    # Assert that the measured resource distribution of the perfectly distributed layout is 0
    assert measure_resource_distribution(Board(terrain_types=perfectly_distributed_layout['terrain_types'],
                                               tile_numbers=perfectly_distributed_layout['tile_numbers'])) == 0


def test_measure_resource_clustering():
    # Assert that the measured resource clustering of each known layout is correct
    for layout_data in known_clustered_layouts:
        assert measure_resource_clustering(Board(terrain_types=layout_data[0]['terrain_types'],
                                                 tile_numbers=layout_data[0]['tile_numbers'])) == layout_data[1]


def test_measure_probability_distribution_per_resources():
    # Assert that the measured resource clustering of each known layout is correct
    for layout_data in known_probability_distribution_layouts:
        assert round(measure_probability_distribution_per_resources(Board(terrain_types=layout_data[0]['terrain_types'],
                                                                          tile_numbers=layout_data[0]['tile_numbers'])),
                     4) == round(layout_data[1], 4)


def test_measure_probability_distribution_on_board():
    # Assert that the measured resource clustering of each known layout is correct
    for layout_data in known_probability_distribution_on_board_layouts:
        assert measure_probability_distribution_on_board(Board(terrain_types=layout_data[0]['terrain_types'],
                                                               tile_numbers=layout_data[0]['tile_numbers'])) == \
               layout_data[1]


def test_measure_probability_clustering():
    # Assert that the measured resource clustering of each known layout is correct
    for layout_data in known_probability_clustering_layouts:
        assert measure_probability_clustering(Board(terrain_types=layout_data[0]['terrain_types'],
                                                    tile_numbers=layout_data[0]['tile_numbers'])) == layout_data[1]
