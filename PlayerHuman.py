from ErrorMessage import ErrorMessage
from Player import Player
from UserInput import UserInput

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
                game.board.print_probability(self.symbol)
                continue
