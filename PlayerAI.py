from Player import Player, PlayerSymbol

try:
    from audioop import minmax
except ImportError:
    from audioop import minmax as minmax

class PlayerAI(Player):
    def get_move(self, board) -> str:
        depth = 9 - len(board.get_valid_moves())
        is_maximizing = True
        
        self.minmax(board, depth, is_maximizing)
        
    def minmax(self, board, depth, is_maximizing):
        opponent_symbol = (PlayerSymbol.O.value
                               if self.symbol == PlayerSymbol.X.value
                               else PlayerSymbol.X.value)
        
        def evaluate_board(board):
            game_over, winner = board.is_game_over()
            
            if game_over is False or winner == 'draw':
                return 0
            elif winner == self.symbol:
                return 1
            else:
                return -1
        
        eval = evaluate_board(board)

        if is_maximizing:
            max_eval = float('-inf')
            for move in board.get_valid_moves():
                new_board = board.update_board(move, self.symbol)
                eval = self.minmax(new_board, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.get_valid_moves():
                new_board = board.update_board(move, opponent_symbol)
                eval = self.minmax(new_board, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval
    