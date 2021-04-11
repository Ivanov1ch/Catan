from catan.balance.calculate_balance import get_balance_values
from catan.generation.generate_board import generate_random_board

# Generates num_to_generate random catan.board.Boards using catan.gernation.generate_board.generate_random_board() and
# tracks the highest outputted value for each key in catan.balance.calculate_balance.get_balance_values() across
# every generation. This is used to get a decent estimate of the upper limits of each measurement, which will then
# be updated into catan.balance.calculate_balance's upper_limits dictionary to normalize the balance scores outputted
# by catan.balance.calculate_balance.calculate_balance(catan.board.Board) onto  the [0.0, 1.0] range
num_to_generate = 5 * 10 ** 5

# The dictionary containing the current maximum values for each measurement (same keys as in measurement_dictionary)
current_maximums = None

for board_num in range(num_to_generate):
    generated_board = generate_random_board()
    measurement_dictionary = get_balance_values(generated_board)

    if current_maximums is None:
        current_maximums = measurement_dictionary  # Every first value is a current maximum value
    else:
        # Determine if any of measurement_dictionary's values are larger and update current_maximums accordingly
        current_maximums = {measurement: max(current_maximums[measurement], measurement_dictionary[measurement]) for
                            measurement in list(measurement_dictionary.keys())}

    print("Generated {0} of {1}".format(board_num + 1, num_to_generate))

# Output the final value of current_maximums
print(current_maximums)
