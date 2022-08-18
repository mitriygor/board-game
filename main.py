from config.board_config import BoardConfig
from utils.board_validator import BoardValidator
from fboard import FBoard

"""
Initialization of the board for demo
"""


def init_board():
    board_config = BoardConfig()
    config = board_config.get_board_config()
    board_validator = BoardValidator()
    f_board = FBoard(config, board_validator)
    f_board.print_board()


if __name__ == '__main__':
    init_board()
