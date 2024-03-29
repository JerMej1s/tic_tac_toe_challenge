from typing import Optional

from Board import Board
from Player import Player
from Timer import Timer, TimeUnit
from User import ErrorMessage, UserInput
from UserInterface import UserInterface

ui = UserInterface()
probability_timer = Timer(TimeUnit.NANOSECONDS)

class PlayerHuman(Player):
    def get_move(self, board: Board) -> Optional[str]:
        valid_moves: list[str] = board.get_valid_moves()

        probability_timer.start()
        win_probability: float = round(
            board.get_win_probability(self.symbol) * 100, 2
        )
        probability_duration: float = round(probability_timer.stop(), 2)

        while True:
            ui.print_board_timestamp(board.updated_at)
            ui.print_board(board.board)
            ui.print_probability(
                self.symbol,
                win_probability,
                probability_duration
            )

            user_input: str = input(
                f"Player {self.symbol}, enter a number {valid_moves} " +
                "or 'q' to quit: "
            ).lower()

            if user_input in valid_moves:
                move = user_input
                break
            elif user_input == UserInput.QUIT.value:
                move = None
                break
            else:
                print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                continue

        return move
