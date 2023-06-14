class GameException(Exception):
    pass


class BoardException(GameException):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "The shot out of bounds"


class CellBusyException(BoardException):
    def __str__(self):
        return "The cell is busy"


class RepeatedFireException(BoardException):
    def __str__(self):
        return "The cell has already been shot"


class IncorrectInputException(GameException):
    def __str__(self):
        return "Incorrect input. Try again"
