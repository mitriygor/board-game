import unittest
from tests.data.valid_config import ValidConfig
from utils.board_validator import BoardValidator
from fboard import FBoard


class TestBoardValidator(unittest.TestCase):
    def test_move(self):
        valid_config = ValidConfig()
        config = valid_config.get_board_config()
        board_validator = BoardValidator()
        f_board = FBoard(config, board_validator)
        f_board.print_board()
        self.assertTrue(f_board.move_x(1, 1))
        f_board.print_board()


if __name__ == '__main__':
    unittest.main()
