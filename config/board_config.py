"""
A generic data class which contains initial data for the board. In order to make the board configurable, it doesn't contains
hardcoded information. All information could be injected externally. THe config contains:

    boundaries - a set of predefined limits within which moves are allowed. The maximum boundary is used as the size of
    the board, which has square-shape.

    init_moves - a set of initial moves for each player. The initial moves are used to setting up the board.

    directions - a set of allowed directions for each player. In current setup of the game, the X-player has 4 allowed
    directions diagonally, and the O-payer has 3 allowed directions, as well - diagonally.

    symbols - a set of symbols used for each player. In order to make the game even more customizable, the symbols could
    be changed through configurations as well.
"""


class BoardConfig:
    __boundaries = [0, 8]
    __init_moves = {"x": [[0, 0]], "o": [[5, 7], [6, 6], [7, 5], [7, 7]]}
    __directions = {"x": [[-1, -1], [-1, 1], [1, -1], [1, 1]], "o": [[-1, -1], [-1, 1], [1, -1]]}
    __symbols = {
        "x": "x",
        "o": "o",
        "placeholder": "-",
    }

    def get_board_config(self):
        return {
            "boundaries": self.__boundaries,
            "init_moves": self.__init_moves,
            "directions": self.__directions,
            "symbols": self.__symbols,
        }
