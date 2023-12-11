from enum import Enum

class PlayerSymbol(Enum):
    X = 'X'
    O = 'O'

class Player:
    def __init__(self):
        self.symbol = None # Not used when the computer isn't playing

    def get_move(self, game) -> str:
        pass