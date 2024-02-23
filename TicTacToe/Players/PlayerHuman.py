from typing import Optional

from TicTacToe.Board import Board
from TicTacToe.Game import PlayerSymbol
from TicTacToe.Players.Player import Player
from TicTacToe.Services.Timer import Timer, TimeUnit
from TicTacToe.Services.Timer import Timer, TimeUnit
from TicTacToe.User import ErrorMessage, UserInput
from TicTacToe.UserInterface import UserInterface


ui = UserInterface()
probability_timer = Timer(TimeUnit.NANOSECONDS)


class PlayerHuman(Player):
    def __init__(self, symbol: PlayerSymbol) -> None:
        super().__init__(symbol=symbol)

    def get_move(self, board: Board) -> Optional[str]:
        valid_moves: list[str] = board.get_valid_moves()
        if not valid_moves:
            raise ValueError('No valid moves available.')

        probability_timer.start()
        win_probability: float = round(
            board.get_win_probability(self.symbol) * 100,
            2
        )
        probability_duration: float = round(probability_timer.stop(), 2)

        move: Optional[str] = None
        while True:
            ui.print_board_timestamp(updated_time=board.updated_at)
            ui.print_board(board=board.board)
            ui.print_probability(
                player_symbol=self.symbol,
                probability=win_probability,
                duration=probability_duration
            )

            user_input: str = input(
                f"Player {self.symbol.value}, enter a number {valid_moves} or " +
                f"{UserInput.QUIT.value} to {UserInput.QUIT.name.lower()}: "
            ).strip().lower()

            if user_input in valid_moves:
                move = user_input
                break
            elif user_input == UserInput.QUIT.value:
                break
            else:
                print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                continue

        return move
