from datetime import datetime
from typing import Optional

from Board import Board
from Game import Game, PlayerSymbol
from Players.PlayerComputer import PlayerComputer
from Players.PlayerHuman import PlayerHuman
from Services.DataService import DataService
from Services.Timer import Timer, TimeUnit
from User import DifficultyLevel, User
from UserInterface import UserInterface

ui = UserInterface()
user = User()
human_player = PlayerHuman()
game = Game()
board = Board()
program_timer = Timer()
game_timer = Timer()
turn_timer = Timer()
data_service = DataService()

program_timer.start()
ui.print_game_start_message(start_time=datetime.now())

is_playing: bool = True

while is_playing:
    # Determine if computer is playing
    is_computer_playing: Optional[bool] = user.is_computer_playing()

    if is_computer_playing:
        # Determine players' symbols
        is_computer_first: Optional[bool] = user.does_computer_go_first()
        if is_computer_first is None:
            # User is quitting
            is_playing = False
            break
        human_player.symbol = (PlayerSymbol.O
            if is_computer_first
            else PlayerSymbol.X
        )
        computer_symbol = (PlayerSymbol.X
            if is_computer_first
            else PlayerSymbol.O
        )
        computer_player = PlayerComputer(symbol=computer_symbol)

        # Determine difficulty level
        difficulty_level: Optional[DifficultyLevel] = user.get_difficulty_level()
        if difficulty_level is None:
            # User is quitting
            is_playing = False
            break
        computer_player.difficulty_level = difficulty_level
    elif is_computer_playing is None:
        # User is quitting
        is_playing = False
        break

    # Start game
    is_first_turn: bool = True
    is_game_over: bool = False
    game.current_player = PlayerSymbol.X # always goes first

    board.reset_board()
    game_timer.start()

    while not is_game_over:
        if not is_first_turn:
            game.switch_player()

        # Get current player's move
        player_move: Optional[str] = None

        if (is_computer_playing
            and game.current_player == computer_player.symbol
        ):
            # Computer player's turn
            turn_timer.unit = TimeUnit.NANOSECONDS
            turn_timer.start()
            player_move = computer_player.get_move(board=board)
        else:
            # Human player's turn
            human_player.symbol = game.current_player
            turn_timer.unit = TimeUnit.SECONDS
            turn_timer.start()
            player_move = human_player.get_move(board=board)

        if player_move is None:
            # User is quitting
            is_playing = False
            break

        # Make move
        board.update_board(
            player_symbol=game.current_player,
            cell=player_move
        )

        # End turn
        turn_duration: float = round(turn_timer.stop(), 2)
        game.tabulate_turn_duration(turn_duration=turn_duration)
        is_first_turn = False

        if len(board.get_valid_moves()) <= 4:
            # Check if game is over
            is_game_over, game.winner = board.is_game_over()

    # Game is over or user is quitting
    game.duration = round(game_timer.stop(), 2)
    ui.print_board(board=board.board)

    if board.is_game_over():
        ui.print_winner(winner=game.winner)
        ui.print_game_details(
            game=game,
            end_time=board.updated_at,
            is_computer_playing=is_computer_playing,
            human_symbol=human_player.symbol
        )
        data_service.save_game_data(game=game)

    if is_playing:
        is_playing = user.is_playing_again()

# User is quitting or not playing again
game_history: list[Game] = data_service.get_historical_game_data()
if game_history:
    ui.print_historical_game_data(game_history=game_history)
    data_service.delete_historical_game_data()

ui.print_game_end_message(end_time=datetime.now())

program_run_time = round(program_timer.stop(), 2)
ui.print_end_program_message(run_time=program_run_time)
