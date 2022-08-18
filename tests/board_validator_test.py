import unittest
from tests.data.valid_config import ValidConfig
from tests.data.valid_move import ValidMove
from utils.board_validator import BoardValidator


class TestBoardValidator(unittest.TestCase):
    def test_valid_config(self):
        valid_config = ValidConfig()
        config = valid_config.get_board_config()
        board_validator = BoardValidator()
        self.assertTrue(board_validator.is_config_valid(config))

    def test_valid_move(self):
        valid_move = ValidMove()
        mode = valid_move.get_board_config()
        board_validator = BoardValidator()
        self.assertTrue(board_validator.is_move_valid(
            mode["move"],
            mode["boundaries"],
            mode["board"],
            mode["directions"],
            mode["symbol"]
        ))


if __name__ == '__main__':
    unittest.main()
