# A dictionary mapping each number token value to how many of each appear in the base game
number_token_distribution = {
    2: 1,
    3: 2,
    4: 2,
    5: 2,
    6: 2,
    8: 2,
    9: 2,
    10: 2,
    11: 2,
    12: 1
}

# A dictionary mapping each number token value to how many dots appear beneath it
number_token_dots = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1
}


# The class representing a number token on the board
class NumberToken:
    def __init__(self, number):
        self.number = number

        if number < 2 or number > 12 or number == 7 or not isinstance(number, int):
            raise ValueError("Number tokens must have integer values between 2 and 12, inclusive, excluding 7!")

        self.dot_count = number_token_dots[number]

    def __str__(self):
        return '{0} ({1} dots)'.format(self.number, self.dot_count)
