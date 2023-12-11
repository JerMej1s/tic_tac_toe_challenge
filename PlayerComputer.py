import random

from PlayerHuman import PlayerHuman
from PlayerSymbol import PlayerSymbol

class ComputerPlayer(PlayerHuman):
    def get_move(self, board) -> str:
        valid_moves = board.get_valid_moves()

        def check_for_win(symbol) -> str:
            for valid_move in valid_moves:
                board.update_board(valid_move, symbol)
                
                game_over, _ = board.is_game_over()

                if game_over:
                    board.clear_cell(valid_move)
                    return valid_move
                else:
                    board.clear_cell(valid_move)
            
            valid_move = None
            
            return valid_move

        # Try to win
        move = check_for_win(self.symbol)

        if move is None:
            # Block opponent's win
            opponent_symbol = (PlayerSymbol.O.value
                               if self.symbol == PlayerSymbol.X.value
                               else PlayerSymbol.X.value)
            move = check_for_win(opponent_symbol)

        if move is None:
            # Choose a random move
            move = str(random.choice(valid_moves))

        return move
