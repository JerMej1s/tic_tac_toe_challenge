import random

from Player import Player, PlayerSymbol

class PlayerComputer(Player):
    def get_move(self, board) -> str:
        new_board = board
        valid_moves = new_board.get_valid_moves()

        def check_for_win(symbol) -> str:
            best_move = None

            for valid_move in valid_moves:
                new_board.update_board(valid_move, symbol)
                
                is_game_over, _ = new_board.is_game_over()

                if is_game_over:
                    new_board.clear_cell(valid_move)
                    best_move = valid_move
                    break
                else:
                    new_board.clear_cell(valid_move)
                    continue
            
            return best_move

        # Try to win
        move = check_for_win(self.symbol)

        if move is None:
            # Block opponent's win
            opponent_symbol = (PlayerSymbol.O.value
                               if self.symbol == PlayerSymbol.X.value
                               else PlayerSymbol.X.value)
            move = check_for_win(opponent_symbol)

        if move is None:
            # Choose a random corner or center
            center_and_corners = ['1', '3', '5', '7', '9']
            valid_center_and_corners = ([corner for corner 
                                         in center_and_corners
                                         if corner in valid_moves])
            
            if len(valid_center_and_corners) > 0:
                move = str(random.choice(valid_center_and_corners))

        if move is None:
            # Choose a random move
            move = str(random.choice(valid_moves))

        return move
