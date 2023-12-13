from enum import Enum

class PlayerSymbol(Enum):
    X = 'X'
    O = 'O'

class Player:
    def __init__(self):
        self.symbol = None # Do not use in human vs. human games.
                           # Instead, use game.curent_player.

    def get_move(self, game) -> str:
        pass