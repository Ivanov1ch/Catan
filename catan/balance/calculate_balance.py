from catan.balance.probability_clustering import measure_probability_clustering
from catan.balance.probability_distribution_on_board import measure_probability_distribution_on_board
from catan.balance.probability_distribution_per_resource import measure_probability_distribution_per_resources
from catan.balance.resource_clustering import measure_resource_clustering
from catan.balance.resource_distribution import measure_resource_distribution

# The upper limits for each measurement, used to normalize them all on the [0.0, 1.0] range
# These are the outputs of catan.generation.determine_upper_limits (specifically with num_to_generate = 5 * 10 ** 5)
upper_limits = {
    'resource_distribution': 4536,
    'resource_clustering': 90.0,
    'probability_clustering': 40.0,
    'probability_distribution_per_resources': 109.92592592592594,
    'probability_distribution_on_board': 40932
}


# Outputs a number on the range [0.0, 1.0] that represents how balanced this board is, with 0 being perfectly balanced
# and 1 being the worst possibly balanced board.
def calculate_balance(board):
    # The process behind each of these methods was inspired by Board Game Analysis's blog post:
    # https://www.boardgameanalysis.com/what-is-a-balanced-catan-board/

    balance_values = get_balance_values(board)

    # Normalize balance values
    balance_values = {measurement: balance_values[measurement] / upper_limits[measurement]
                      for measurement in list(balance_values.keys())}

    # Return the average of these normalized values
    normalized_values = list(balance_values.values())
    return sum(normalized_values) / len(normalized_values)


# Outputs a dictionary with all of the measured values that would go into a calculate_balance(board) calculation
# This is mainly used to determine the upper limits of each score in brute-force generation test runs in
# catan.generation.determine_upper_limits.py
def get_balance_values(board):
    return {
        'resource_distribution': measure_resource_distribution(board),
        'resource_clustering': measure_resource_clustering(board),
        'probability_clustering': measure_probability_clustering(board),
        'probability_distribution_per_resources': measure_probability_distribution_per_resources(board),
        'probability_distribution_on_board': measure_probability_distribution_on_board(board)
    }
