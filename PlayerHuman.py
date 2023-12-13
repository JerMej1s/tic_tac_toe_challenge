from Player import Player

class PlayerHuman(Player):
    def get_move(self, board) -> str:
        valid_moves = board.get_valid_moves()

        user_input = input(f"Player {self.symbol}, " +
                            f"enter a number {valid_moves} " +
                            f"or 'q' to quit: ").lower()
    
        return user_input
