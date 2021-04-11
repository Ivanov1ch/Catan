import math


# Much of this code is slightly modified from resource_distribution.py

# Divides the island into equal parts and analyzes the probabilities surrounding SettlementLocations, three times
def measure_probability_distribution_on_board(board):
    # For convenience
    settlements = board.settlement_locations
    # Calculate for horizontal division (horizontal line through the center of the board) - split into two groups
    top_half = []
    bottom_half = []

    for row in range(math.ceil(len(settlements) / 2)):
        top_row = settlements[row]
        bottom_row = settlements[len(settlements) - 1 - row]

        # Due to the symmetric nature of a Catan board, top_row and bottom_row will have the same lengths
        for index in range(len(top_row)):
            top_half.append(top_row[index])
            bottom_half.append(bottom_row[index])

    # Calculate the resource distribution score for this horizontal division
    horizontal_division_score = calculate_probability_distribution_score(top_half, bottom_half)

    # Calculate for the positive-slope diagonal division (from bottom left to top right)
    left_half_positive = []
    right_half_positive = []

    # And also for the negative-slope diagonal division (from top left to bottom right)
    left_half_negative = []
    right_half_negative = []

    # Populate these arrays
    # This is essentially a row-by-row operation, as there is not a solid coordinate system to work with

    # A dictionary mapping each index in settlements to how many SettlementLocations lie to the right of the
    # positive-slope dividing line or to the left of the negative-slope dividing line in the TOP HALF of the board.
    # This will be used to call fill_arrays_from_sides and populate the left and right half arrays.
    # Only indices 0-5 are mapped because the vertical symmetry is utilized to manage the other half
    row_to_num_on_side = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 2,
        5: 3
    }

    # Use the items in the dictionary to call fill_arrays_from_sides
    for settlement_row, num_right in row_to_num_on_side.items():
        fill_arrays_from_sides(left_half_positive, right_half_positive, left_half_negative, right_half_negative,
                               settlements, settlement_row, num_right)

    # Calculate the resource distribution score for these divisions
    positive_slope_division_score = calculate_probability_distribution_score(left_half_positive, right_half_positive)
    negative_slope_division_score = calculate_probability_distribution_score(left_half_negative, right_half_negative)

    # Calculate and return the final result by summing the scores for each of the 3 divisions
    return horizontal_division_score + positive_slope_division_score + negative_slope_division_score


# Adds SettlementLocations from settlements (A Board's settlement_locations) in the row in the TOP HALF of the board,
# settlement_row, to the left and right-side groups for the positive-slope diving line, left_arr_pos and right_arr_pos,
# of SettlementLocations. num_on_side is an integer, indicating how many SettlementLocations on this row (in the TOP
# HALF) are on the right side of the positive-slope line or on the left side of the negative-slope line. This method
# utilizes the vertical symmetry of the board to also add the SettlementLocations from the row vertically opposite to
# settlement_row.
def fill_arrays_from_sides(left_arr_pos, right_arr_pos, left_arr_neg, right_arr_neg, settlements,
                           settlement_row, num_on_side):
    bottom_settlement_row = len(settlements) - 1 - settlement_row

    for col in range(len(settlements[settlement_row]) - num_on_side):
        bottom_col = len(settlements[bottom_settlement_row]) - 1 - col

        # Fill for positive-slope dividing line
        left_arr_pos.append(settlements[settlement_row][col])
        right_arr_pos.append(settlements[bottom_settlement_row][bottom_col])

        # Fill in reverse for negative-slope dividing line
        right_arr_neg.append(settlements[settlement_row][col])
        left_arr_neg.append(settlements[bottom_settlement_row][bottom_col])

    for col in range(num_on_side):
        # Fill for positive-slope dividing line
        left_arr_pos.append(settlements[bottom_settlement_row][col])
        right_arr_pos.append(settlements[settlement_row][len(settlements[settlement_row]) - 1 - col])

        # Fill in reverse for negative-slope dividing line
        right_arr_neg.append(settlements[bottom_settlement_row][col])
        left_arr_neg.append(settlements[settlement_row][len(settlements[settlement_row]) - 1 - col])


# Calculates the probability distribution score across the two provided groups (lists) of SettlementLocations.
# This is done in the following method:
#   1) Sum the number of dots from the NumberTokens for each TerrainHex surrounding this SettlementLocation
#   2) Sum these sums for each SettlementLocation in each half (in each group)
#   3) Take the difference between these sums
#   4) Square this difference and return it
def calculate_probability_distribution_score(group_one, group_two):
    # Calculate the group probability sums of both groups (1 & 2)
    group_one_sums = calculate_group_probability_sums(group_one)
    group_two_sums = calculate_group_probability_sums(group_two)

    # Square the difference and return it (3 & 4)
    return (group_one_sums - group_two_sums) ** 2


def calculate_group_probability_sums(group):
    group_sum = 0

    for settlement_location in group:
        # Sum the number of dots under each surrounding NumberToken
        for number_token in settlement_location.surrounding_number_tokens:
            group_sum += number_token.dot_count

    return group_sum
