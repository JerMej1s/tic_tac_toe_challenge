import datetime
from typing import Optional

from TicTacToe.Board import Board
from TicTacToe.Game import Game, PlayerSymbol
from TicTacToe.Services.Timer import TimeUnit


class UserInterface:
    def __init__(self):
        pass

    def print_game_start_message(self, start_time: datetime) -> None:
        print("\nHello world! The game started at " +
            f"{start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}." +
            "\n\nLet's play Tic Tac Toe!"
        )

    def print_board_timestamp(self, updated_time: datetime) -> None:
        print(
            "\nThe game board was last updated at " +
            f"{updated_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}."
        )

    def print_board(self, board: Board) -> None:
        print("\n")
        print("\n".join(
            ["|".join(board[i:i+3]) for i in range(0, 9, 3)]
        ))
        print("\n")

    def print_probability(
            self,
            player_symbol: PlayerSymbol,
            probability: float,
            duration: float
        ) -> None:
        print(f"Player {player_symbol.value} has a {probability}% probability " +
            f"to win, which took {duration} nanoseconds to calculate."
        )

    def print_winner(self, winner: Optional[PlayerSymbol]) -> None:
        if winner == None:
            print("It's a draw!\n")
        else:
            print(f"Player {winner.value} wins!\n")

    def print_game_details(
            self,
            game: Game,
            end_time: datetime,
            is_computer_playing: bool,
            human_symbol: PlayerSymbol
        ) -> None:
        x_time_unit = (
            TimeUnit.NANOSECONDS.value
            if is_computer_playing and human_symbol == PlayerSymbol.O
            else TimeUnit.SECONDS.value
        )
        o_time_unit = (
            TimeUnit.NANOSECONDS.value
            if is_computer_playing and human_symbol == PlayerSymbol.X
            else TimeUnit.SECONDS.value
        )

        print(f"Player {PlayerSymbol.X.value} " +
            f"took {round(game.player_x_turn_duration, 2)} " +
            f"{x_time_unit} to play. " +
            f"Player {PlayerSymbol.O.value} " +
            f"took {round(game.player_o_turn_duration, 2)} " +
            f"{o_time_unit} to play. " +
            f"Game took {game.duration} seconds to play, " +
            f"ending at {end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}."
        )

    def print_historical_game_data(self, game_history: list[Game]) -> None:
        x_win_count: int = len([
            game for game in game_history
            if game.winner == PlayerSymbol.X
        ])
        o_win_count: int = len([
            game for game in game_history
            if game.winner == PlayerSymbol.O
        ])

        game_count: int = len(game_history)
        x_win_percentage: float = round(x_win_count / game_count * 100, 2)
        o_win_percentage: float = round(o_win_count / game_count * 100, 2)

        total_x_turn_duration: float = 0
        total_o_turn_duration: float = 0

        print("\nGame History:" +
            "\n-------------\n"
        )

        for game in game_history:
            game_num: int = game_history.index(game) + 1

            x_turn_duration: float = round(game.player_x_turn_duration, 2)
            o_turn_duration: float = round(game.player_o_turn_duration, 2)

            total_x_turn_duration += game.player_x_turn_duration
            total_o_turn_duration += game.player_o_turn_duration

            if game.winner == "draw":
                winner_message: str = "it was a draw"
            else:
                winner_message: str = f"{game.winner} won"

            print(f"Game {game_num} took {game.duration} seconds " +
                f"to play and {winner_message}. " +
                f"{PlayerSymbol.X.value} took {x_turn_duration} seconds " +
                "to play and " +
                f"{PlayerSymbol.O.value} took {o_turn_duration} seconds " +
                "to play."
            )

        # TODO: Handle case with mixed time units for same player,
        #       i.e., multiple-game sessions where the computer
        #       played as X and O.
        print(f"\nOut of {game_count} game(s), " +
            f"{PlayerSymbol.X.value} won {x_win_percentage}% and " +
            f"{PlayerSymbol.O.value} won {o_win_percentage}%. " +
            "Congratulations!\n" +
            f"{PlayerSymbol.X.value} took a total of {x_turn_duration} " +
            "seconds to play and " +
            f"{PlayerSymbol.O.value} took a total of {o_turn_duration} " +
            "seconds to play.\n")

    def print_game_end_message(self, end_time: datetime) -> None:
        print("\nThe game ended at " +
            f"{end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}." +
            "\n\nThanks for playing! Goodbye world!"
        )

    def print_end_program_message(self, run_time: datetime) -> None:
        print(f"\nProgram was running for {run_time} seconds.\n")
