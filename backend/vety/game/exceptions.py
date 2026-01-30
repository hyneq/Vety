"""
Game-related exceptions
"""

class GameException(Exception):
    """
    A base class for game-related exceptions.
    """


class GameAlreadyFinishedException(GameException):
    """
    The game has already finished
    """


class GameNotFinishedYetException(GameException):
    """
    The game has not finished yet
    """
