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
