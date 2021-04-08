# A class representing a potential settlement location on the board (a vertex of a TerrainHex, or a vertex shared
# between multiple TerrainHexes)
class SettlementLocation:
    # Constructor. surrounding_terrain_hexes is an array of the TerrainHexes that have this SettlementLocation on any
    # one of their vertices
    def __init__(self, surrounding_terrain_hexes):
        if type(surrounding_terrain_hexes) is list:
            self.surrounding_terrain_hexes = surrounding_terrain_hexes

            # Generate a list of surrounding ResourceTypes and a dictionary mapping each ResourceType's value to how
            # many TerrainHexes producing that ResourceType are available from this SettlementLocation
            self.available_resources = []

            # Generates the dict {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
            self.available_resource_distribution = {k: 0 for k in list(range(1, 6))}

            for terrain_hex in surrounding_terrain_hexes:
                if terrain_hex.terrain_type.value != 0:
                    resource_type = terrain_hex.terrain_type.get_resource_type()
                    self.available_resources.append(resource_type)
                    self.available_resource_distribution[resource_type.value] += 1

    def __str__(self):
        out = ''
        for tile in self.surrounding_terrain_hexes:
            out += str(tile)
            out += ', '

        return out
