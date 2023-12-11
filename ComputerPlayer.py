import random

from Player import Player
from typing import Optional

class ComputerPlayer(Player):
    def __init__(self):
        pass
    
    def is_computer_playing(self) -> Optional[bool]:
        while True:
            user_input = input("Do you want to play against the computer? " +
                            "[y/n or q to quit]: ").lower()
            
            if user_input == 'y':
                return True
            elif user_input == 'n':
                return False
            elif user_input == 'q':
                return None
            else:
                print("Invalid input. Please try again.")
                continue

    def does_computer_go_first(self) -> bool:
        while True:
            user_input = input("\nDo you want to go first? " +
                                "[y/n or q to quit]: ").lower()
            
            if user_input == 'y':
                self.symbol = 'O'
                return False
            elif user_input == 'n':
                self.symbol = 'X'
                return False
            elif user_input == 'q':
                return None
            else:
                print("Invalid input. Please try again.")
                continue

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
            opponent_symbol = 'O' if self.symbol == 'X' else 'X'
            move = check_for_win(opponent_symbol)

        if move is None:
            # Choose a random move
            move = str(random.choice(valid_moves))

        return move
