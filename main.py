from flask import *

from catan.board.terrain_hexes import terrain_hex_distribution
from catan.generation.generate_board import generate_balanced_board, generate_unbalanced_board

# How many random boards to test in generate_balanced_board and generate_unbalanced_board:
# The higher this value is, the better and more consistent the results will be (at the expense of generation time)
num_random = 10 ** 4

# How many hexes and how many number tokens should be on a Catan board. See render_generated_board() for usage and more.
num_hexes = sum(list(terrain_hex_distribution.values()))
num_number_tokens = num_hexes - terrain_hex_distribution['DESERT']

app = Flask(__name__)


# Render home page
@app.route('/')
def render_home_page():
    return render_template('index.html')


# Render generated board, if the right GET parameters are provided
@app.route('/view-board', methods=['GET'])
def render_generated_board():
    # Read get parameters
    hexes = request.args.get('hexes')
    numbers = request.args.get('numbers')
    score = request.args.get('score')

    # If one of the parameters is missing, send the user back to the home page
    if hexes is None or numbers is None or score is None:
        return redirect('/', code=307, Response=None)

    # Split into arrays of strings
    hexes_arr = hexes.split(',')
    numbers_arr = numbers.split(',')

    # Check if the lengths of these arrays are correct:
    # There should be as many items in hexes_arr as there are TerrainHexes in the game
    # There should be len(hexes_arr) - the number of deserts in the game items in numbers_arr, as deserts have no
    # NumberTokens on them.
    #
    # The number of TerrainHexes in the game and the number of deserts were pulled from terrain_hex_distribution
    #
    # If either length is incorrect, redirect to the home page
    if len(hexes_arr) != num_hexes or len(numbers_arr) != num_number_tokens:
        return redirect('/', code=307, Response=None)

    # Convert to integers and floats
    try:
        converted_hexes_arr = list(map(int, hexes_arr))
        converted_numbers_arr = list(map(int, numbers_arr))
        converted_score = float(score)

        # Finally, check if the converted score is in the proper generated range. If not, redirect to the home page
        if converted_score < 0 or converted_score > 1:
            return redirect('/', code=307, Response=None)

        # If we have reached this point, everything is valid! Render the page with the parsed data
        return render_template('view_board.html', terrain_hex_arr=converted_hexes_arr,
                               number_token_arr=converted_numbers_arr, score=converted_score)
    except ValueError:
        # One of the values is not a number, thus the parameters are invalid and the user should be redirected home
        return redirect('/', code=307, Response=None)


# Listen and comply to board generation requests
@app.route('/generate-board', methods=['POST'])
def api_generate_board():
    req_json = request.get_json(silent=True)

    generating_balanced = req_json['isBalanced']

    generated_board, board_balance_score = generate_balanced_board(
        num_random) if generating_balanced else generate_unbalanced_board(num_random)

    terrain_hexes, number_tokens = generated_board.get_board_arrays()

    # Build the URL to redirect to the board-viewing page with the board's data passed into the GET parameters
    redirect_url = '/view-board?hexes={0}&numbers={1}&score={2}'.format(','.join(map(str, terrain_hexes)),
                                                                        ','.join(map(str, number_tokens)),
                                                                        board_balance_score)

    return_data = {
        'status': 'ok',
        'code': 200,
        'redirect_url': redirect_url
    }

    return jsonify(return_data)


if __name__ == "__main__":
    app.run()
