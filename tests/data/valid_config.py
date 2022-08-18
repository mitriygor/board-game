class ValidConfig:
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
