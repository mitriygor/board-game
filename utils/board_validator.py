from config.board_error import ConfigBoundariesError, ConfigInitMoveError, ConfigDirectionsError, ConfigSymbolsError

"""
Class provides generic validation for data, e.g. it verifies if move is within the max and min boundaries
"""


class BoardValidator:
    """
    Method provides general validation of configurations

    TODO: replace generic exceptions
    """

    def is_config_valid(self, config) -> bool:
        is_every_boundary_valid = False
        is_every_init_move_valid = False
        is_every_direction_valid = False
        is_every_symbol_valid = False

        try:
            is_every_boundary_valid = self.__is_every_boundary_valid(config["boundaries"])
        except Exception:
            raise ConfigBoundariesError()

        if is_every_boundary_valid:
            try:
                is_every_init_move_valid = self.__is_every_init_move_valid(config["init_moves"], config["boundaries"])
            except Exception:
                raise ConfigInitMoveError()

        if is_every_init_move_valid:
            try:
                is_every_direction_valid = self.__is_every_direction_valid(config["directions"])
            except Exception:
                raise ConfigDirectionsError()

        if is_every_direction_valid:
            try:
                is_every_symbol_valid = self.__is_every_symbol_valid(config["symbols"])
            except Exception:
                raise ConfigSymbolsError()

        return is_every_symbol_valid

    """
    Validation of provided move. The move is validated against boundaries, i.e. if it is within the boundaries, and,
    in addition, against the surrounding elements, i.e. there is supposed to be at least one neighbour of the same type.
    In order to make validation flexible and re-usable, the method accepts a dictionary of arguments. In the dictionary,
    there could be expected:
    
    move - list containing two integer values for row and column;
    
    boundaries - list with minimal and maximal acceptable values for the moves within current board;
    
    board - two-dimensional list which represents the board. It contains all moves;
    
    directions - available directions for actual player, i.e. either X or O player;
    
    symbol - symbol which represent current player ;
    """

    def is_move_valid(self, **kwargs) -> bool:
        move = kwargs.get("move")
        boundaries = kwargs.get("boundaries")
        board = kwargs.get("board")
        directions = kwargs.get("directions")
        symbol = kwargs.get("symbol")
        return self.__is_every_coordinate_valid(move, boundaries) and \
               self.__is_position_valid(move, boundaries, board, directions, symbol)

    """
    Validation of an initial move which used to setting up the board. The initial moves are allowed to have no neighbors
    of the same type; therefore, the positioning validation was skipped. THe method has similarity with is_move_valid
    method, but it needs less arguments, so it works only with two:
    
    move - two-integers list with row and column values;
    
    boundaries - list with minimal and maximal acceptable values for the moves within current board;
    
    """

    def is_init_move_valid(self, **kwargs) -> bool:
        move = kwargs.get("move")
        boundaries = kwargs.get("boundaries")
        return self.__is_every_coordinate_valid(move, boundaries)

    """
    Validation of surrounding elements in order to identify at least one neighbour of the same type based on available 
    directions. The method is made private.
    """

    def __is_position_valid(self, move, boundaries, board, directions, symbol: str) -> bool:

        positions = list(map(lambda direction: [direction[0] + move[0], direction[1] + move[1]], directions))
        return any((self.__is_every_coordinate_valid(pos, boundaries) and
                    board[pos[0]][pos[1]] == symbol) for pos in positions)

    """
    A static method which validates coordinates against boundaries. The method's name contains the 'every'-word in order
    to keep the same 'is'-prefix for the bool-returning method. Otherwise, there would be necessary to introduce 
    new prefixes, e.g. 'are', 'has', etc. (e.g. 'are_coordinates_valid', 'has_valid_coordinates'). Consistency in naming
     helps to make code more readable which is very important, after all, we read code more often than write code.
    """

    @staticmethod
    def __is_every_coordinate_valid(move, boundaries) -> bool:
        return all((isinstance(coordinate, int) and boundaries[0] <= coordinate < boundaries[1]) for coordinate in move)

    """
    A static method which validates boundaries. Boundaries are supposed to be presented by two integers, and the first one
    is supposed to be smaller than the last one. The method is used to validate the initial configuration.
    """

    @staticmethod
    def __is_every_boundary_valid(boundaries) -> bool:
        return all((isinstance(boundary, int)) for boundary in boundaries) and boundaries[0] < boundaries[1]

    """
    The method verifies moves which used for the board setting up. The method is used within the initial verification of
    the config. 
    """

    def __is_every_init_move_valid(self, init_moves, boundaries) -> bool:

        return all(all(self.__is_every_coordinate_valid(move, boundaries) for move in moves) for player, moves in
                   init_moves.items())

    """
    The method verifies presence of the directions for each player.
    """

    @staticmethod
    def __is_every_direction_valid(directions) -> bool:
        return len(directions["x"]) > 0 and len(directions["o"]) > 0

    """
    General validation for the symbols for the board.
    """

    @staticmethod
    def __is_every_symbol_valid(symbols) -> bool:
        return symbols["x"] and symbols["o"] and symbols["placeholder"]
