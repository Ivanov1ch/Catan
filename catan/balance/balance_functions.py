from catan.balance.resource_distribution import measure_resource_distribution


# Inspired by Board Game Analysis's blog post: https://www.boardgameanalysis.com/what-is-a-balanced-catan-board/

def calculate_balance(board):
    return measure_resource_distribution(board)
