from catan.board.terrain_hexes import TerrainType

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

# Contains the four board layouts with known clustering scores, in an array with their known score
known_clustered_layouts = [
    # No clustering at all - no adjacent TerrainHexes have the same TerrainType
    [{
        'terrain_types': [TerrainType.FIELD, TerrainType.FOREST, TerrainType.FIELD, TerrainType.FOREST,
                          TerrainType.PASTURE, TerrainType.HILL, TerrainType.PASTURE, TerrainType.PASTURE,
                          TerrainType.FIELD, TerrainType.MOUNTAIN, TerrainType.FIELD, TerrainType.HILL,
                          TerrainType.MOUNTAIN, TerrainType.DESERT, TerrainType.HILL, TerrainType.MOUNTAIN,
                          TerrainType.FOREST, TerrainType.PASTURE, TerrainType.FOREST],
        # The numbers don't matter here - just copy beginner_layout's
        'tile_numbers': beginner_layout['tile_numbers']
    }, 0],
    [{
        'terrain_types': [TerrainType.PASTURE, TerrainType.HILL, TerrainType.HILL, TerrainType.FOREST,
                          TerrainType.MOUNTAIN, TerrainType.PASTURE, TerrainType.MOUNTAIN, TerrainType.PASTURE,
                          TerrainType.FIELD, TerrainType.FOREST, TerrainType.FIELD, TerrainType.MOUNTAIN,
                          TerrainType.FIELD, TerrainType.FOREST, TerrainType.PASTURE, TerrainType.DESERT,
                          TerrainType.FOREST, TerrainType.FIELD, TerrainType.HILL],
        # The numbers don't matter here - just copy beginner_layout's
        'tile_numbers': beginner_layout['tile_numbers']
    }, 25],
    [{
        'terrain_types': [TerrainType.PASTURE, TerrainType.FOREST, TerrainType.FOREST, TerrainType.MOUNTAIN,
                          TerrainType.FOREST, TerrainType.HILL, TerrainType.MOUNTAIN, TerrainType.FIELD,
                          TerrainType.MOUNTAIN, TerrainType.HILL, TerrainType.HILL, TerrainType.FOREST,
                          TerrainType.FIELD, TerrainType.FIELD, TerrainType.DESERT, TerrainType.FIELD,
                          TerrainType.PASTURE, TerrainType.PASTURE, TerrainType.PASTURE],
        # The numbers don't matter here - just copy beginner_layout's
        'tile_numbers': beginner_layout['tile_numbers']
    }, 50],
    [{
        'terrain_types': [TerrainType.FIELD, TerrainType.FIELD, TerrainType.DESERT, TerrainType.FIELD,
                          TerrainType.FIELD, TerrainType.PASTURE, TerrainType.HILL, TerrainType.MOUNTAIN,
                          TerrainType.HILL, TerrainType.MOUNTAIN, TerrainType.PASTURE, TerrainType.PASTURE,
                          TerrainType.FOREST, TerrainType.FOREST, TerrainType.HILL, TerrainType.PASTURE,
                          TerrainType.FOREST, TerrainType.FOREST, TerrainType.HILL],
        # The numbers don't matter here - just copy beginner_layout's
        'tile_numbers': beginner_layout['tile_numbers']
    }, 75],
    # Just about as clustered as it gets
    [{
        'terrain_types': [TerrainType.PASTURE, TerrainType.PASTURE, TerrainType.DESERT, TerrainType.PASTURE,
                          TerrainType.PASTURE, TerrainType.FIELD, TerrainType.FIELD, TerrainType.MOUNTAIN,
                          TerrainType.MOUNTAIN, TerrainType.HILL, TerrainType.FIELD, TerrainType.FIELD,
                          TerrainType.MOUNTAIN, TerrainType.HILL, TerrainType.FOREST, TerrainType.FOREST,
                          TerrainType.HILL, TerrainType.FOREST, TerrainType.FOREST],
        # The numbers don't matter here - just copy beginner_layout's
        'tile_numbers': beginner_layout['tile_numbers']
    }, 100],
]

# Contains the four board layouts with known clustering scores, in an array with their known score
known_probability_distribution_layouts = [
    # Very well distributed board, asserted value calculated manually
    [{
        'terrain_types': [TerrainType.FOREST, TerrainType.FIELD, TerrainType.FOREST, TerrainType.HILL,
                          TerrainType.MOUNTAIN,
                          TerrainType.FOREST, TerrainType.HILL, TerrainType.MOUNTAIN, TerrainType.HILL,
                          TerrainType.FIELD,
                          TerrainType.PASTURE, TerrainType.PASTURE, TerrainType.PASTURE, TerrainType.MOUNTAIN,
                          TerrainType.FIELD, TerrainType.DESERT, TerrainType.PASTURE, TerrainType.FOREST,
                          TerrainType.FIELD],
        'tile_numbers': [5, 11, 9, 12, 3, 10, 8, 6, 4, 8, 4, 9, 5, 10, 2, 3, 11, 6]
    }, 16 / 27],
    # Decently distributed board, asserted value calculated manually
    [{
        'terrain_types': [TerrainType.MOUNTAIN, TerrainType.FOREST, TerrainType.PASTURE, TerrainType.FIELD,
                          TerrainType.FOREST, TerrainType.FIELD, TerrainType.MOUNTAIN, TerrainType.PASTURE,
                          TerrainType.DESERT, TerrainType.FOREST, TerrainType.HILL, TerrainType.HILL, TerrainType.FIELD,
                          TerrainType.FOREST, TerrainType.MOUNTAIN, TerrainType.PASTURE, TerrainType.PASTURE,
                          TerrainType.FIELD, TerrainType.HILL],
        'tile_numbers': [4, 5, 4, 6, 11, 9, 3, 2, 3, 11, 6, 8, 12, 10, 9, 5, 8, 10]
    }, 1516 / 27],
    # Very badly distributed board, asserted value calculated manually
    [{
        'terrain_types': [TerrainType.FIELD, TerrainType.FOREST, TerrainType.FOREST, TerrainType.PASTURE,
                          TerrainType.FIELD, TerrainType.DESERT, TerrainType.FIELD, TerrainType.MOUNTAIN,
                          TerrainType.PASTURE, TerrainType.HILL, TerrainType.PASTURE, TerrainType.MOUNTAIN,
                          TerrainType.FIELD, TerrainType.HILL, TerrainType.HILL, TerrainType.MOUNTAIN,
                          TerrainType.FOREST, TerrainType.PASTURE, TerrainType.FOREST],
        'tile_numbers': [6, 9, 5, 2, 5, 8, 4, 11, 10, 12, 10, 6, 3, 3, 4, 9, 11, 8]
    }, 2950 / 27],
]
