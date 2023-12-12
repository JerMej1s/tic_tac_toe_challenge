from datetime import datetime

from ErrorMessage import ErrorMessage
from Player import PlayerSymbol
from Timer import TimeUnit
from UserInput import UserInput

class UserInterface:
    def __init__(self):
        self.is_computer_playing = None

    def get_timestamp(self) -> str:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    
    def print_game_start_message(self) -> None:
        print(f"\nHello world! The game started at {self.get_timestamp()}." +
              "\n\nLet's play Tic Tac Toe!")

    def print_game_end_message(self) -> None:
        print(f"\nThe game ended at {self.get_timestamp()}!\n\n" +
              "Thanks for playing! Goodbye world!")
 
    def print_board_timestamp(self) -> None:
        print("\n" +
              f"The game board was last updated at {self.get_timestamp()}.")

    def play_with_computer(self) -> None:
        while True:
            user_input = input("\nDo you want to play against the computer? " +
                            "[y/n or q to quit]: ").lower()
            
            if user_input == UserInput.YES.value:
                self.is_computer_playing = True
                break
            elif user_input == UserInput.NO.value:
                self.is_computer_playing = False
                break
            elif user_input == UserInput.QUIT.value:
                break
            else:
                print(ErrorMessage.INVALID_INPUT.value)
                continue
            
    def does_computer_go_first(self) -> (bool, PlayerSymbol):
        while True:
            user_input = input("\nDo you want to go first? " +
                                "[y/n or q to quit]: ").lower()
            
            if user_input == UserInput.YES.value:
                symbol = PlayerSymbol.O.value
                return False, symbol
            elif user_input == UserInput.NO.value:
                symbol = PlayerSymbol.X.value
                return False, symbol
            elif user_input == UserInput.QUIT.value:
                return None, None
            else:
                print(ErrorMessage.INVALID_INPUT.value)
                continue

    def is_playing_again(self) -> bool:
        while True:
            user_input = (input("\nDo you want to play again? [y/n/q]: ")
                            .lower())
            
            if (user_input == UserInput.NO.value
                or user_input == UserInput.QUIT.value):
                return False
            elif user_input == UserInput.YES.value:
                return True
            else:
                print(ErrorMessage.INVALID_INPUT.value)
                continue

    def print_game_details(self, game, symbol) -> None:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        x_time_unit = (TimeUnit.MILLISECONDS.value
                       if self.play_with_computer
                       and symbol == PlayerSymbol.X.value
                       else TimeUnit.SECONDS.value)
        o_time_unit = (TimeUnit.MILLISECONDS.value
                       if self.play_with_computer
                       and symbol == PlayerSymbol.O.value
                       else TimeUnit.SECONDS.value)
        
        print(f"Player X took {round(game.player_x_turn_duration, 2)} " +
                f"{x_time_unit} to play. " +
                f"Player O took {round(game.player_o_turn_duration, 2)} " +
                f"{o_time_unit} to play. " +
                f"Game took {game.duration} seconds to play, " +
                f"ending at {now}.")

    def print_historical_game_data(self, game_history) -> None:
        game_count = len(game_history)

        x_win_count = len(([game for game in game_history
                            if game.winner == PlayerSymbol.X.value]))
        o_win_count = len(([game for game in game_history
                            if game.winner == PlayerSymbol.O.value]))
        
        x_win_percentage = round(x_win_count / game_count * 100, 2)
        o_win_percentage = round(o_win_count / game_count * 100, 2)

        total_x_turn_duration = 0
        total_o_turn_duration = 0

        print("\nGame History:" +
                "\n-------------\n")
        
        for game in game_history:
            game_num = game_history.index(game) + 1

            x_turn_duration = round(game.player_x_turn_duration, 2)
            o_turn_duration = round(game.player_o_turn_duration, 2)

            total_x_turn_duration += game.player_x_turn_duration
            total_o_turn_duration += game.player_o_turn_duration

            if game.winner == "draw":
                winner_message = "it was a draw"
            else:
                winner_message = f"{game.winner} won"
            
            print(f"Game {game_num} took {game.duration} seconds " +
                    f"to play and {winner_message}. " +
                    f"X took {x_turn_duration} seconds to play and " +
            f"O took {o_turn_duration} seconds to play.")

        # TODO: Handle case with mixed time units for same player,
        #       i.e., multiple-game sessions where the computer
        #       played as X and O.
        print(f"\nOut of {game_count} game(s), " +
            f"X won {x_win_percentage}% and " +
            f"O won {o_win_percentage}%. Congratulations!\n" +
            f"X took a total of {x_turn_duration} seconds to play and " +
            f"O took a total of {o_turn_duration} seconds to play.\n")
            