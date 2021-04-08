# Generates a score for how clustered a Board's TerrainHexes are, with 0 for a board with no clustering
# (no two adjacent TerrainHexes produce the same resource) and a score around 100 for a board with complete
# clustering (each resource type is in a homogeneous "blob"). This is done by adding 5 points for each edge shared by
# two TerrainHexes of the same resource type
def measure_resource_clustering(board):
    # A counter for the number of unique edges shared by two TerrainHexes that produce the same resource
    # After the following for loop executes, this value will be divided by 2 to get the final edge count
    num_shared_edges = 0

    # Iterate over every SettlementLocation to extract all of the available_resource_distribution dictionaries
    for settlement_location_row in board.settlement_locations:
        for settlement_location in settlement_location_row:
            resource_dist = settlement_location.available_resource_distribution

            # Get the values of each key-value pair into one list
            adjacent_resource_count = list(resource_dist.values())

            # For each resource type, adjust num_shared_edges as follows:
            #   If there are 0 or 1 adjacent TerrainHexes, leave it as it is
            #   If there are 2 adjacent TerrainHexes, increment it  by 1 (settlement_location is the endpoint of 1 edge)
            #   If there are 3 adjacent TerrainHexes, increment it by 3 (settlement_location is the endpoint of 3 edges)
            for adjacency_count in adjacent_resource_count:
                if adjacency_count == 2:
                    num_shared_edges += 1
                elif adjacency_count == 3:
                    num_shared_edges += 3
                # No need for an else statement here, as possible values range from 0-3, inclusive

    # Now convert this value of num_shared_edges into the true number of shared edges by dividing by 2
    # We divide by two because there are two SettlementLocations (two endpoints) for every edge
    num_shared_edges /= 2

    # The final score can be calculated by multiplying the number of shared edges by 5
    return num_shared_edges * 5
