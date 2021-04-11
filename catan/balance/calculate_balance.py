from catan.balance.probability_distribution_per_resource import measure_probability_distribution_per_resources
from catan.balance.resource_clustering import measure_resource_clustering
from catan.balance.resource_distribution import measure_resource_distribution


# The process behind each of these methods was inspired by Board Game Analysis's blog post:
# https://www.boardgameanalysis.com/what-is-a-balanced-catan-board/

def calculate_balance(board):
    resource_distribution_score = measure_resource_distribution(board)
    resource_clustering_score = measure_resource_clustering(board)
    probability_distribution_score = measure_probability_distribution_per_resources(board)
    return resource_distribution_score
