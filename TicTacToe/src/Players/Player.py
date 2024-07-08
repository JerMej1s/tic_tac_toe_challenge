from typing import Optional

from TicTacToe.src.Board import Board
from TicTacToe.src.Game import PlayerSymbol


class Player:
    def __init__(self):
        self.symbol: PlayerSymbol = None

    def get_move(self, board: Board) -> Optional[str]:
        board: Board = board

