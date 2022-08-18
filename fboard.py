from config.game_state import GameState
import traceback

""""
Class FBoard contains private data labeled with dunders, i.e. double underscores. In order to make the class customizable,
and the game more flexible, there is an option to provide configurations, so the board size, symbols and other parameters
could be re-defined. The class contains next properties:

    game_state - represents current state of the game. Type of the Enum based GameState;
    
    game_state - represents current state of the game. Type of the Enum based GameState;
    
    directions - values of allowed directions for each player;
    
    symbols - a dictionary with symbols which used on the board. Its values is configurable. Preservation the symbols 
    within a dictionary helps to avoid hardcoded strings within the class;
    
    board - actual board. It is a square of the maximum boundaries value;

As result of providing values through configurations, the class doesn't contains "magic numbers" or hardcoded strings.

TODO: replace generic exceptions
"""


class FBoard:
    __game_state: GameState

    def __init__(self, config, validator):
        try:
            self.__validator = validator
            self.__boundaries = config["boundaries"]
            self.__directions = config["directions"]
            self.__symbols = config["symbols"]
            self.__board = [[self.__symbols["placeholder"] for col in range(self.__boundaries[1])] for row in
                            range(self.__boundaries[1])]

            self.__game_state = GameState.UNFINISHED

            self.__set_multiple_moves(config["init_moves"]["x"], self.__directions["x"], self.__symbols["x"])
            self.__set_multiple_moves(config["init_moves"]["o"], self.__directions["o"], self.__symbols["o"])

        except Exception:
            traceback.print_exc()

    """
    Method to print/show the board
    """

    def print_board(self):
        print("\n".join(["".join(["{:4}".format(symbol) for symbol in row]) for row in self.__board]))

    """
    Standard getter for a private property game_state
    """

    def get_game_state(self) -> GameState:
        return self.__game_state

    """
    A method which exposes a piece of functionality responsible for the X-player moves. Based on X-related parameters,
    the method calls a private move-method.
    """

    def move_x(self, row: int, col: int) -> bool:
        return self.__move(row, col, self.__directions["x"], self.__symbols["x"], self.__validator.is_move_valid)

    """
    The same as move_x method but for O-player
    """

    def move_o(self, row: int, col: int) -> bool:
        return self.__move(row, col, self.__directions["o"], self.__symbols["o"], self.__validator.is_move_valid)

    """
    In order to avoid code duplication, a piece of functionality responsible for moves is unified in one private method.
    It accepts coordinates, i.e. row and column, and player-type  related data. All data passes through validation.
    """

    def __move(self, row: int, col: int, directions, symbol: str, is_move_valid) -> bool:
        if self.__game_state == GameState.UNFINISHED:
            move = [row, col]
            if is_move_valid(move=move, boundaries=self.__boundaries, board=self.__board, directions=directions,
                             symbol=symbol):
                self.__board[row][col] = symbol
                self.__update_game_state(move, symbol)
                return True
        return False

    """
    A private method which updates state of the game based on provided coordinates after each move
    """

    def __update_game_state(self, move, symbol: str):
        try:
            if move[0] == self.__boundaries[1] - 1 and move[1] == self.__boundaries[1] - 1:
                self.__game_state = GameState.X_WON if symbol == self.__symbols["x"] else GameState.O_WON

        except Exception:
            traceback.print_exc()

    """
    The method provides functionality to set multiple moves. Present usage of the method in setting up initial state of
    the board.
    """

    def __set_multiple_moves(self, moves, directions, symbol: str):
        for move in moves:
            self.__move(move[0], move[1], directions, symbol, self.__validator.is_init_move_valid)
