from enum import Enum

"""
 Usage of Enums could help to prevent misspellings an overriding data.
 In the current setup, the game could have one of the three state: either one of two players won, or undefined.
"""


class GameState(Enum):
    X_WON = 1
    O_WON = 2
    UNFINISHED = 3
