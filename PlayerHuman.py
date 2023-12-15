from typing import Optional

from Player import Player
from Timer import Timer, TimeUnit
from UserInterface import ErrorMessage, UserInput, UserInterface

ui = UserInterface()
probability_timer = Timer(TimeUnit.NANOSECONDS)

class PlayerHuman(Player):
    def get_move(self, board) -> Optional[str]:
        valid_moves = board.get_valid_moves()

        probability_timer.start()
        win_probability = (round(
            board.get_win_probability(self.symbol) * 100, 2))
        probability_duration = probability_timer.stop()

        while True:
            ui.print_board_timestamp(board.updated_at)
            ui.print_board(board.board)
            ui.print_probability(self.symbol, win_probability,
                                 probability_duration)

            user_input = input(f"Player {self.symbol}, " +
                               f"enter a number {valid_moves} " +
                               f"or 'q' to quit: ").lower()

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
