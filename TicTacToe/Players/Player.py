from typing import Optional

from TicTacToe.Board import Board
from TicTacToe.Game import PlayerSymbol


class Player:
    def __init__(self, symbol: Optional[PlayerSymbol]=None) -> None:
        self.symbol = symbol

    def get_move(self, board: Board) -> Optional[str]:
        board = board
