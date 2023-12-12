from ErrorMessage import ErrorMessage
from Player import Player
from Probability import Probability
from UserInput import UserInput

probability = Probability()

class PlayerHuman(Player):
    def get_move(self, game) -> str:
        valid_moves = game.board.get_valid_moves()

        while True:
            user_input = input(f"Player {game.current_player}, " +
                                f"enter a number {valid_moves} " +
                                f"or 'q' to quit: ").lower()
            
            if (user_input in valid_moves
                or user_input == UserInput.QUIT.value):
                return user_input
            else:
                print(ErrorMessage.INVALID_INPUT.value)
                game.board.print_board()
                probability.print_probability(game)
                continue
