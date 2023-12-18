from enum import Enum
from typing import Optional

from Board import Board

class PlayerSymbol(Enum):
    X = 'X'
    O = 'O'

class Player:
    def __init__(self):
        self.symbol = None

    def get_move(self, board: Board) -> Optional[str]:
        pass