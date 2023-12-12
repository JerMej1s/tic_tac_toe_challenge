from Player import Player, PlayerSymbol

try:
    from audioop import minmax
except ImportError:
    from audioop import minmax as minmax

class PlayerAI(Player):
    def get_move(self, board) -> str:
        new_board = board
        valid_moves = new_board.get_valid_moves()
        
        best_score = float('-inf')
        best_move = None
        
        depth = 1 # 9 - len(board.get_valid_moves())
        is_maximizing = True
                
        def minmax(another_new_board, depth, is_maximizing):
            opponent_symbol = (PlayerSymbol.O.value
                                if self.symbol == PlayerSymbol.X.value
                                else PlayerSymbol.X.value)
            
            def evaluate_board():
                game_over, winner = another_new_board.is_game_over()
                
                if game_over is False or winner == 'draw':
                    return 0
                elif winner == self.symbol:
                    return 1
                else:
                    return -1
            
            eval = evaluate_board()

            if is_maximizing:
                max_eval = float('-inf')
                for move in another_new_board.get_valid_moves():
                    new_board = another_new_board.update_board(move, self.symbol)
                    
                    if new_board is None:
                        print(f"Failed to generate new board with move {move} and symbol {self.symbol}")
                    else:
                        eval = minmax(new_board, depth - 1, False)
                    
                    # eval = self.minmax(new_board, depth - 1, False)
                    max_eval = max(max_eval, eval)
                
                return max_eval
            else:
                min_eval = float('inf')
                for move in another_new_board.get_valid_moves():
                    new_board = another_new_board.update_board(move, opponent_symbol)
                    
                    if new_board is None:
                        print(f"Failed to generate new board with move {move} and symbol {self.symbol}")
                    else:
                        eval = self.minmax(new_board, depth - 1, True)
                        
                    # eval = self.minmax(new_board, depth - 1, True)
                    min_eval = min(min_eval, eval)
                
                return min_eval
        
        minmax(new_board, depth, is_maximizing)
        
        for valid_move in valid_moves:
            new_board = board.update_board(valid_move, self.symbol)
            score = minmax(new_board, depth, is_maximizing)
            
            if score > best_score:
                best_score = score
                best_move = valid_move
        
        return best_move
        
    