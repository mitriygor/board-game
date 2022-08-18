"""
Collection of error classes
"""

class ConfigBoundariesError(Exception):

    def __init__(self, message="Provided boundaries are invalid"):
        self.message = message
        super().__init__(self.message)


class ConfigInitMoveError(Exception):

    def __init__(self, message="Provided within config init moves are invalid"):
        self.message = message
        super().__init__(self.message)

class ConfigDirectionsError(Exception):

    def __init__(self, message="Provided directions are invalid"):
        self.message = message
        super().__init__(self.message)

class ConfigSymbolsError(Exception):

    def __init__(self, message="Provided symbols are invalid"):
        self.message = message
        super().__init__(self.message)


class BoardInitError(Exception):

    def __init__(self, message="Provided symbols are invalid"):
        self.message = message
        super().__init__(self.message)
