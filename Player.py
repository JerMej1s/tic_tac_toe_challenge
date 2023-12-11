class Player:
    def __init__(self):
        self.symbol = None

    def get_move(self, board) -> str:
        valid_moves = board.get_valid_moves()

        while True:
            user_input = input(f"Player {self.symbol}, " +
                                f"enter a number {valid_moves} " +
                                f"or 'q' to quit: ")
            
            if user_input in valid_moves or user_input.lower() == 'q':
                return user_input
            else:
                print("\nInvalid input. Please try again.")
                board.print_board()
                board.print_probability(self.symbol)
                continue
