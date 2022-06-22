import json
import os
import shutil
from catan.board.terrain_hexes import TerrainType
from catan.generation.generate_board import generate_balanced_board, generate_unbalanced_board
from colour import Color

if __name__ == '__main__':
    num_boards_to_generate = 2 * 10 ** 3
    num_to_test = 10 ** 4
    balance_color_range = list(Color('#228b22').range_to(Color('#ff0000'), 101))
    svg_class_conversions = {terrain_type.value: terrain_type.name.lower() for terrain_type in TerrainType}

    folder_path = os.path.join('static', 'generated')
    balanced_path = os.path.join(folder_path, 'balanced.json')
    unbalanced_path = os.path.join(folder_path, 'unbalanced.json')
    conversions = os.path.join(folder_path, 'svg_class_conversions.json')

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

    os.mkdir(folder_path)

    with open(conversions, 'w+') as file:
        json.dump(svg_class_conversions, file)

    balanced_data = {
        "num_boards": 0,
        "boards": []
    }

    unbalanced_data = {
        "num_boards": 0,
        "boards": []
    }


    def update_data(generated_board, board_score, board_data):
        terrain_hexes, number_tokens = generated_board.get_board_arrays()

        board_data["num_boards"] = board_data["num_boards"] + 1
        board_data["boards"].append({
            "hexes": ','.join(map(str, terrain_hexes)),
            "numbers": ','.join(map(str, number_tokens)),
            "score": board_score,
            "color": balance_color_range[round(round(board_score, 2) / 0.01)].hex[1:]
        })

    try:
        for i in range(num_boards_to_generate):
            generated_balanced_board, balanced_board_balance_score = generate_balanced_board(num_to_test)
            generated_unbalanced_board, unbalanced_board_balance_score = generate_unbalanced_board(num_to_test)

            update_data(generated_balanced_board, balanced_board_balance_score, balanced_data)
            update_data(generated_unbalanced_board, unbalanced_board_balance_score, unbalanced_data)
            print("Generated board pair #" + str(i + 1))

        with open(balanced_path, 'w+') as balanced_file:
            json.dump(balanced_data, balanced_file)

        with open(unbalanced_path, 'w+') as unbalanced_file:
            json.dump(unbalanced_data, unbalanced_file)

    except:
        with open(balanced_path, 'w+') as balanced_file:
            json.dump(balanced_data, balanced_file)

        with open(unbalanced_path, 'w+') as unbalanced_file:
            json.dump(unbalanced_data, unbalanced_file)
