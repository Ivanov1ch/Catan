from number_tokens import NumberToken
from settlement_location import SettlementLocation
from terrain_hexes import TerrainHex, TerrainType


# A class representing and containing the methods of a Catan board
class Board:
    # terrain_types: a one-dimensional array of integers, each corresponding to a TerrainType (see TerrainType).
    #                It should be in an order that starts goes left to right, from the top of the board to the bottom of
    #                the board, and will be translated into self.hexes.
    # tile_numbers: a one-dimensional array of integers, in the same order as terrain_types. Represents the numbers
    #                on each TerrainHex at the corresponding location. Skip the desert.
    def __init__(self, terrain_types=None, tile_numbers=None):
        # The two-dimensional array storing the layout of the tiles on the field
        self.hexes = [[None] * 3, [None] * 4, [None] * 5, [None] * 4, [None] * 3]

        # The two-dimensional array storing the layout of SettlementLocations
        self.settlement_locations = []

        if terrain_types is None and tile_numbers is None:
            raise ValueError("Either a terrain_types or tile_numbers array must be provided")

        if (terrain_types is not None and len(terrain_types) != 19) or (
                tile_numbers is not None and len(tile_numbers) != 18):
            raise ValueError("Improper terrain_types or tile_numbers length (should be 19 and 18)")

        if terrain_types is not None:
            self.translate_hexes_arr(terrain_types, tile_numbers=tile_numbers)
            self.generate_settlement_locations()

    def translate_hexes_arr(self, terrain_types, tile_numbers=None):
        # A counter indicating where in the iteration through terrain_types the loop currently is
        terrain_index = 0
        # A counter indicating where in the iteration through tile_index the loop currently is
        tile_index = 0

        for row in range(len(self.hexes)):
            for col in range(len(self.hexes[row])):
                # Instantiates a TerrainHex, turning the int in terrain_types into its corresponding TerrainType first
                terrain = TerrainHex(TerrainType(terrain_types[terrain_index]))

                # Link a NumberToken instance to this TerrainHex if possible
                if tile_numbers is not None:
                    # Skips
                    if terrain.terrain_type is not TerrainType.DESERT:
                        terrain.number_token = NumberToken(tile_numbers[tile_index])
                        tile_index += 1

                self.hexes[row][col] = terrain
                terrain_index += 1

    def generate_settlement_locations(self):
        current_index = 0
        self.settlement_locations = [None] * 12

        # Execute the following code twice, once with multiplier = 1 and once with multiplier = -1
        # This allows us to take advantage of the symmetry of the board when populating settlement_locations
        for multiplier in range(1, -2, -2):
            # Top row has vertices of that are only adjacent to one tile
            row_one = []

            for i in range(3):
                row_one.append(SettlementLocation([self.hexes[2 - multiplier * 2][i]]))

            self.settlement_locations[current_index] = row_one
            current_index += multiplier

            # Second row of vertices has 2 unique and 2 shared SettlementLocations
            row_two = [SettlementLocation([self.hexes[2 - multiplier * 2][0]])]
            for i in range(1, 3):
                surrounding_terrain_hexes = [self.hexes[2 - multiplier * 2][i - 1], self.hexes[2 - multiplier * 2][i]]
                row_two.append(SettlementLocation(surrounding_terrain_hexes))
            row_two.append(SettlementLocation([self.hexes[2 - multiplier * 2][2]]))

            self.settlement_locations[current_index] = row_two
            current_index += multiplier

            # Third row of vertices has 4 shared SettlementLocations
            row_three = []
            for i in range(4):
                surrounding_terrain_hexes = [self.hexes[2 - multiplier * 1][i]]
                if i == 0 or i == 3:
                    surrounding_terrain_hexes.append(self.hexes[2 - multiplier * 2][i if i == 0 else i - 1])
                else:
                    surrounding_terrain_hexes.extend(
                        [self.hexes[2 - multiplier * 2][i - 1], self.hexes[2 - multiplier * 2][i]])

                row_three.append(SettlementLocation(surrounding_terrain_hexes))

            self.settlement_locations[current_index] = row_three
            current_index += multiplier

            # Fourth row of vertices has 2 unique and 3 shared SettlementLocations
            row_four = [SettlementLocation([self.hexes[2 - multiplier * 1][0]])]
            for i in range(1, 4):
                surrounding_terrain_hexes = [self.hexes[2 - multiplier * 2][i - 1], self.hexes[1][i - 1],
                                             self.hexes[1][i]]
                row_four.append(SettlementLocation(surrounding_terrain_hexes))

            row_four.append(SettlementLocation([self.hexes[2 - multiplier * 1][3]]))
            self.settlement_locations[current_index] = row_four
            current_index += multiplier

            # Fifth row of vertices has 5 shared SettlementLocations
            row_five = []

            for i in range(5):
                surrounding_terrain_hexes = [self.hexes[2][i]]

                if i == 0 or i == 4:
                    surrounding_terrain_hexes.append(self.hexes[2 - multiplier * 1][i if i == 0 else i - 1])
                else:
                    surrounding_terrain_hexes.extend(
                        [self.hexes[2 - multiplier * 1][i - 1], self.hexes[2 - multiplier * 1][i]])

                row_five.append(SettlementLocation(surrounding_terrain_hexes))

            self.settlement_locations[current_index] = row_five
            current_index += multiplier

            # Sixth row of vertices has 2 unique and 4 shared SettlementLocations
            row_six = [SettlementLocation([self.hexes[2][0]])]

            for i in range(1, 5):
                surrounding_terrain_hexes = [self.hexes[2 - multiplier * 1][i - 1], self.hexes[2][i - 1],
                                             self.hexes[2][i]]
                row_six.append(SettlementLocation(surrounding_terrain_hexes))

            row_six.append(SettlementLocation([self.hexes[2][4]]))
            self.settlement_locations[current_index] = row_six

            current_index = len(self.settlement_locations) - 1 if multiplier == 1 else 0
