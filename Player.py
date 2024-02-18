from typing import Optional

from Board import Board

class Player:
    def __init__(self):
        self.symbol: str = None

    def get_move(self, board: Board) -> Optional[str]:
        board: Board = board