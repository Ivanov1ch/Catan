from enum import Enum


# An enum for each type of resource produced by a terrain hex
class ResourceType(Enum):
    ORE = 1
    LUMBER = 2
    GRAIN = 3
    WOOL = 4
    BRICK = 5


# An enum for each type of terrain included in the base game
class TerrainType(Enum):
    DESERT = 0
    MOUNTAIN = 1
    FOREST = 2
    FIELD = 3
    PASTURE = 4
    HILL = 5

    # Maps a TerrainType to its produced ResourceType
    def get_resource_type(self):
        return ResourceType(self.value)


# A dictionary mapping each TerrainType to how many of each appear in the base game
terrain_hex_distribution = {
    'DESERT': 1,
    'MOUNTAIN': 3,
    'FOREST': 4,
    'FIELD': 4,
    'PASTURE': 4,
    'HILL': 3
}


# The class representing a terrain hex on the board
class TerrainHex:
    def __init__(self, terrain_type, number_token=None):
        self.terrain_type = terrain_type
        self.number_token = number_token
