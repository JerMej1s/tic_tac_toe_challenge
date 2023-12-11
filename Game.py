from datetime import datetime

from Board import Board

class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player_x_turn_duration = 0
        self.player_o_turn_duration = 0
        self.current_player = 'X'
        self.winner = None
        self.duration = None

    def start(self) -> None:
        print("\nHello world! Let's play Tic Tac Toe!\n")

    def game_end(self) -> None:
        print("Thanks for playing! Goodbye world!\n")

    def switch_player(self,) -> None:
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def do_play_again(self) -> bool:
        while True:
            user_input = (input("\nDo you want to play again? [y/n/q]: ")
                          .lower())
            
            if user_input == 'n' or user_input == 'q':
                return False
            elif user_input == 'y':
                return True
            else:
                print("Invalid input. Please try again.")
                continue

    def tabulate_turn_duration(self, turn_duration) -> None:
        if self.current_player == 'X':
            self.player_x_turn_duration += turn_duration
        else:
            self.player_o_turn_duration += turn_duration

    def print_winner(self) -> None:
        if self.winner == None:
            return
        elif self.winner == 'draw':
            print("It's a draw!\n")
        else:
            print(f"Player {self.winner} wins!\n")
    
    def print_game_details(self) -> None:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        
        print(f"Player X took {round(self.player_x_turn_duration, 2)} " +
                "seconds to play. " +
              f"Player O took {round(self.player_o_turn_duration, 2)} " +
                "seconds to play. " +
              f"Game took {self.duration} seconds to play, " +
              f"ending at {now}.")
