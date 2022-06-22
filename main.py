from flask import *
from colour import Color
from catan.board.terrain_hexes import terrain_hex_distribution, TerrainType
from catan.generation.generate_board import generate_balanced_board, generate_unbalanced_board

# How many random boards to test in generate_balanced_board and generate_unbalanced_board:
# The higher this value is, the better and more consistent the results will be (at the expense of generation time)
num_random = 10 ** 4

# How many hexes and how many number tokens should be on a Catan board. See render_generated_board() for usage and more.
num_hexes = sum(list(terrain_hex_distribution.values()))
num_number_tokens = num_hexes - terrain_hex_distribution['DESERT']

# A dictionary with keys equal to TerrainType values and values corresponding to the appropriate class to add to the
# <g> tag in static/img/catan_board.svg for a TerrainHex of this TerrainType
svg_class_conversions = {terrain_type.value: terrain_type.name.lower() for terrain_type in TerrainType}

# Use the Colour library to generate a range of colors between green and red, with 101 steps in between. This will be
# used to give a color to the calculated balance value, in increments of 0.01 (green = 0, red = 1)
balance_color_range = list(Color('#228b22').range_to(Color('#ff0000'), 101))

app = Flask(__name__)


# Render home page
@app.route('/')
def render_home_page():
    return render_template('index.html')


# Render generated board, if the right GET parameters are provided
@app.route('/view-board/')
def render_generated_board():
    return render_template('view_board.html')


if __name__ == "__main__":
    app.run()
