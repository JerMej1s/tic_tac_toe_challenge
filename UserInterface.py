import datetime

from Board import Board
from Game import Game, PlayerSymbol
from Timer import TimeUnit

class UserInterface:
    def __init__(self):
        pass
    
    def print_game_start_message(self, datetime: datetime) -> None:
        print(f"\nHello world! The game started at " +
              f"{datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}." +
              "\n\nLet's play Tic Tac Toe!")
 
    def print_board_timestamp(self, datetime: datetime) -> None:
        print("\n" +
              f"The game board was last updated at " +
              f"{datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}.")

    def print_board(self, board: Board) -> None:
        print("\n")
        print("\n".join(["|".join(board[i:i+3])
                        for i in range(0, 9, 3)]))
        print("\n")

    def print_probability(self, player_symbol: PlayerSymbol,
                          probability: float, duration: float) -> None:
        print(f"Player {player_symbol} has a " +
              f"{probability}% chance of winning, " +
              f"which took {duration} nanoseconds to calculate.")

    def print_winner(self, winner: str) -> None:
        if winner == None:
            return
        elif winner == 'draw':
            print("It's a draw!\n")
        else:
            print(f"Player {winner} wins!\n")

    def print_game_details(self, game: Game, datetime: datetime,
                           is_computer_playing: bool,
                           symbol: PlayerSymbol) -> None:
        x_time_unit = (TimeUnit.NANOSECONDS.value
                       if is_computer_playing
                       and symbol == PlayerSymbol.X.value
                       else TimeUnit.SECONDS.value)
        o_time_unit = (TimeUnit.NANOSECONDS.value
                       if is_computer_playing
                       and symbol == PlayerSymbol.O.value
                       else TimeUnit.SECONDS.value)
        
        print(f"Player X took {round(game.player_x_turn_duration, 2)} " +
              f"{x_time_unit} to play. " +
              f"Player O took {round(game.player_o_turn_duration, 2)} " +
              f"{o_time_unit} to play. " +
              f"Game took {game.duration} seconds to play, " +
              f"ending at {datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}.")

    def print_historical_game_data(self, game_history: []) -> None:
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

    def print_game_end_message(self, datetime: datetime) -> None:
        print(f"\nThe game ended at "+
              f"{datetime.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}." +
              "\n\nThanks for playing! Goodbye world!")

    def print_end_program_message(self, run_time: datetime) -> None:
        print(f"\nProgram was running for {run_time} seconds.\n")
