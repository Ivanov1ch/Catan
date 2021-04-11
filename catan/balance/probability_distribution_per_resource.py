from catan.board.terrain_hexes import terrain_hex_distribution, TerrainType


def measure_probability_distribution_per_resources(board):
    # There are 58 total dots across all of the number tiles (the dots being those under the number)
    total_num_dots = 58

    # Calculates how many TerrainHexes there are, excluding the desert
    total_num_hexes = sum(list(terrain_hex_distribution.values())) - terrain_hex_distribution['DESERT']

    # Using this number and the terrain_hex_distribution, we can calculate the expected payout of each TerrainType
    # (minus TerrainType.DESERT) based on how many TerrainHexes with that TerrainType are on the board
    expected_payouts = {terrain_type: terrain_hex_distribution[terrain_type] * total_num_dots / total_num_hexes for
                        terrain_type in list(terrain_hex_distribution.keys()) if terrain_type != 'DESERT'}

    # Count the total number of dots per resource
    terrain_dot_counts = {terrain_type: 0 for terrain_type in list(expected_payouts.keys())}

    # Iterate over every NumberToken (to do this we must iterate over every TerrainHex)
    for terrain_hex_row in board.hexes:
        for terrain_hex in terrain_hex_row:
            if terrain_hex.terrain_type != TerrainType.DESERT:
                number_token = terrain_hex.number_token
                terrain_dot_counts[terrain_hex.terrain_type.name] += number_token.dot_count

    # Calculate the sum of the squares of the differences between actual dots counts and the expected payout
    return sum({terrain_type: (expected_payouts[terrain_type] - terrain_dot_counts[terrain_type]) ** 2
                 for terrain_type in list(expected_payouts.keys())}.values())
