# A class representing a potential settlement location on the board (a vertex of a TerrainHex, or a vertex shared
# between multiple TerrainHexes)
class SettlementLocation:
    # Constructor. surrounding_terrain_hexes is an array of the TerrainHexes that have this SettlementLocation on any
    # one of their vertices
    def __init__(self, surrounding_terrain_hexes):
        if type(surrounding_terrain_hexes) is list:
            self.surrounding_terrain_hexes = surrounding_terrain_hexes
