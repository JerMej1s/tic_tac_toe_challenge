from typing import Optional

from Board import Board

class Player:
    def __init__(self):
        self.symbol = None

    def get_move(self, board: Board) -> Optional[str]:
        pass