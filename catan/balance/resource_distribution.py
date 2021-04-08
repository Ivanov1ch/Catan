import math


# Divides the island into equal parts and analyzes the frequency of available resources, three times
def measure_resource_distribution(board):
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
    horizontal_division_score = calculate_resource_distribution_score(top_half, bottom_half)

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
    positive_slope_division_score = calculate_resource_distribution_score(left_half_positive, right_half_positive)
    negative_slope_division_score = calculate_resource_distribution_score(left_half_negative, right_half_negative)

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


# Calculates the resource distribution score across the two provided groups (lists) of SettlementLocations.
# This is done in the following method:
#   1) Sum the frequency of each available resource across each group (using available_resource_distribution)
#   2) Calculate the difference between each group, for each ResourceType
#   3) Square each resulting difference
#   4) Sum the squares, the result being returned as the final result
def calculate_resource_distribution_score(group_one, group_two):
    # Calculate the group resource sums of both groups (1)
    group_one_sums = calculate_group_resource_sums(group_one)
    group_two_sums = calculate_group_resource_sums(group_two)

    # Calculate and square the difference between the two groups (2 & 3)
    diffs_squared = {k: (group_one_sums.get(k, 0) - group_two_sums.get(k, 0)) ** 2 for k in set(group_one_sums)}

    # Calculate the sum of the squared differences and return it
    sum_of_squares = 0

    for i in range(1, 6):
        sum_of_squares += diffs_squared[i]

    return sum_of_squares


# Generates a dictionary with keys corresponding to ResourceType.values and values corresponding to how the sum of the
# available resource frequencies of each SettlementLocation in the group (group = a list of SettlementLocations)
def calculate_group_resource_sums(group):
    # Generate dictionary to keep track of the sums of the frequencies of each ResourceType (key = ResourceType.value)
    group_sums = {k: 0 for k in list(range(1, 6))}

    # Now iterate over each group and update the group sums accordingly
    for settlement_location in group:
        resource_frequency_count = settlement_location.available_resource_distribution

        # These dictionaries have the same keys, thus we can use a one-liner to combine them via addition
        group_sums = {k: group_sums.get(k, 0) + resource_frequency_count.get(k, 0) for k in
                      set(resource_frequency_count)}

    return group_sums
