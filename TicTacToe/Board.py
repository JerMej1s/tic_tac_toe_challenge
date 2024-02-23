from datetime import datetime
import itertools
from typing import Optional

from TicTacToe.Game import PlayerSymbol

# TODO: Remove duplicate boards and invalid boards.
ALL_BOARDS = set(itertools.permutations('XXXXXOOOO', 9))

WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
]


class Board:
    def __init__(self, board: Optional[list[str]]=None) -> None:
        self.board: list[str] = board or [str(i) for i in range(1, 10)]
        self.possible_boards: set = set()
        self.updated_at: datetime = datetime.now()

    def update_board(self, player_symbol: PlayerSymbol, cell: str) -> None:
        if cell not in [str(i) for i in range(1, 10)]:
            raise ValueError('Invalid cell.')

        cell_index = int(cell) - 1
        if self.board[cell_index] not in [
            PlayerSymbol.X.value, PlayerSymbol.O.value
            ]:
            self.board[cell_index] = player_symbol.value
        else:
            raise ValueError(f'Cell {cell} is already filled ' +
                f'with {self.board[cell_index]}.'
            )
        self.updated_at = datetime.now()

    def clear_cell(self, cell: str) -> None:
        if cell not in [str(i) for i in range(1, 10)]:
            raise ValueError('Invalid cell.')

        self.board[int(cell) - 1] = cell
        self.updated_at = datetime.now()

    def reset_board(self) -> None:
        self.board = [str(i) for i in range(1, 10)]
        self.updated_at = datetime.now()

    def get_valid_moves(self) -> list[str]:
        return [
            i for i in self.board
            if i not in [PlayerSymbol.X.value, PlayerSymbol.O.value]
        ]

    def get_win_probability(self, player_symbol: PlayerSymbol) -> float:
        num_wins: int = 0

        self.possible_boards = set(
            board for board in ALL_BOARDS
            if all(
                b == s for b, s in zip(board, self.board)
                if not s in map(str, range(1, 10))
            )
        )

        possible_wins = (
            set(board for board in self.possible_boards
            if any(
                board[wc[0]] == board[wc[1]] == board[wc[2]]
                for wc in WINNING_COMBINATIONS
            )
        ))

        for possible_win in possible_wins:
            if any(
                possible_win[i] == player_symbol.value
                for wc in WINNING_COMBINATIONS
                for i in wc
            ):
                num_wins += 1

        num_possible_boards: int = len(self.possible_boards)
        win_probability: float = (num_wins / num_possible_boards
            if num_possible_boards else 0
        )

        return win_probability

    def is_game_over(self) -> tuple[bool, Optional[PlayerSymbol]]:
        for wc in WINNING_COMBINATIONS:
            if self.board[wc[0]] == self.board[wc[1]] == self.board[wc[2]]:
                winner_str: str = self.board[wc[0]]

                winner: PlayerSymbol
                if winner_str == PlayerSymbol.X.value:
                    winner = PlayerSymbol.X
                elif winner_str == PlayerSymbol.O.value:
                    winner = PlayerSymbol.O

                return True, winner

        if len(self.get_valid_moves()) == 0:
            return True, None

        return False, None

    def evaluate_score(self, symbol: PlayerSymbol) -> int:
        game_over, winner = self.is_game_over()

        if not game_over:
            raise ValueError('Game is not over.')

        if winner == symbol:
            return 1
        elif winner == None:
            return 0
        else:
            return -1
