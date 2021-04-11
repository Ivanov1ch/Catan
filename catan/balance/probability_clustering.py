# See resource_clustering.py - this is similar to measure_resource_clustering, but this
# adds a score of 5 each time two TerrainHexes with the same number share an edge
#
# This algorithm will be implemented very similarly to measure_resource_clustering (see resource_clustering.py), where
# endpoints will be counted and divided by 2 to get the number of edges. However, as there are at most 2 instances of
# any particular NumberToken on the board, we do not have to deal with the case where a SettlementLocation lies between
# 3 TerrainHexes with the same NumberToken.number - this greatly simplifies the calculation.
def measure_probability_clustering(board):
    # A counter for the number of unique edges shared by two TerrainHexes that have the same NumberToken.number
    # After the following for loop executes, this value will be divided by 2 to get the final edge count
    num_shared_edges = 0

    # Iterate over every SettlementLocation to extract all of the available_resource_distribution dictionaries
    for settlement_location_row in board.settlement_locations:
        for settlement_location in settlement_location_row:
            number_token_dist = settlement_location.number_token_distribution

            # Get the values of each key-value pair into one list
            adjacent_number_token_count = list(number_token_dist.values())

            # If there are 2 of any one NumberToken.number in adjacent_number_token_count, count another endpoint
            for token_count in adjacent_number_token_count:
                if token_count == 2:
                    num_shared_edges += 1
                # No need for an else statement here, as possible values range from 0-2, inclusive

    # Now convert this value of num_shared_edges into the true number of shared edges by dividing by 2
    # We divide by two because there are two SettlementLocations (two endpoints) for every edge
    num_shared_edges /= 2

    # The final score can be calculated by multiplying the number of shared edges by 5
    return num_shared_edges * 5
