# Contains the arrays required to create a Board for the official Catan beginner layout
beginner_layout = {
    'terrain_types': [1, 4, 2, 3, 5, 4, 5, 3, 2, 0, 2, 1, 2, 1, 3, 4, 5, 3, 4],
    'tile_numbers': [10, 2, 9, 12, 6, 4, 10, 9, 11, 3, 8, 8, 3, 4, 5, 5, 6, 11]
}

# Contains the arrays required to create a Board with the perfect resource distribution score (should yield 0)
perfectly_distributed_layout = {
    'terrain_types': [3, 3, 4, 2, 5, 1, 4, 2, 1, 0, 2, 5, 4, 5, 1, 2, 4, 3, 3],
    # The numbers don't matter here - the desert is still in the middle, so just copy beginner_layout
    'tile_numbers': beginner_layout['tile_numbers']
}
