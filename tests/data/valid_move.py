class ValidMove:
    __move = [1, 1]
    __boundaries = [0, 8]
    __board = [["X", "-", "-", "-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-", "-", "-", "-"]]
    __directions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    __symbol = "X"

    def get_board_config(self):
        return {
            "move": self.__move,
            "boundaries": self.__boundaries,
            "board": self.__board,
            "directions": self.__directions,
            "symbol": self.__symbol,
        }
