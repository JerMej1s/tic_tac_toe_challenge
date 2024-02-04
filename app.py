from datetime import datetime

from Board import Board
from DataService import DataService
from Game import Game, PlayerSymbol
from PlayerComputer import PlayerComputer
from PlayerHuman import PlayerHuman
from Timer import Timer, TimeUnit
from User import User
from UserInterface import UserInterface

user = User()
ui = UserInterface()
human_player = PlayerHuman()
computer_player = PlayerComputer()
game = Game()
board = Board()
program_timer = Timer()
game_timer = Timer()
turn_timer = Timer()
data_service = DataService()

program_timer.start()

ui.print_game_start_message(datetime.now())

is_playing = True

while is_playing: # Start a new game
    board.reset_board()
    is_first_turn = True
    is_game_over = False
    
    is_computer_playing = user.is_computer_playing()

    if is_computer_playing: # Determine players' symbols
        is_computer_first = user.does_computer_go_first()
        
        if is_computer_first:
            human_player.symbol = PlayerSymbol.O.value
            computer_player.symbol = PlayerSymbol.X.value
        elif is_computer_first == None: # User entered 'q' to quit
            is_playing = False
            break
        else:
            human_player.symbol = PlayerSymbol.X.value
            computer_player.symbol = PlayerSymbol.O.value
    elif is_computer_playing is None: # User entered 'q' to quit
        is_playing = False
        break

    game_timer.start()

    while not is_game_over:
        if not is_first_turn:
            game.switch_player()

        player_move = None

        if (is_computer_playing and game.current_player == (
            computer_player.symbol)): # Non-human player's turn
            turn_timer.unit = TimeUnit.NANOSECONDS
            turn_timer.start()

            player_move = computer_player.get_move(board)
        else: # Human player's turn
            human_player.symbol = game.current_player
            turn_timer.unit = TimeUnit.SECONDS
            turn_timer.start()
            
            player_move = human_player.get_move(board)

            if player_move is None:
                is_playing = False
                break
            
        if is_playing: # Make player's move, end turn, and check if game over
            board.update_board(player_move, game.current_player)
            
            turn_duration = round(turn_timer.stop(), 2)
            game.tabulate_turn_duration(turn_duration)

            is_first_turn = False

            is_game_over, game.winner = board.is_game_over()
        else:
            break

    if is_playing: # Game is over
        game.duration = round(game_timer.stop(), 2)
        ui.print_board(board.board)
        ui.print_winner(game.winner)
        ui.print_game_details(
            game,
            board.updated_at,
            is_computer_playing,
            computer_player.symbol
        )
        
        data_service.save_game_data(game)

        is_playing = user.is_playing_again()

# User is not playing again
game_history = data_service.get_historical_game_data()

if game_history:
    ui.print_historical_game_data(game_history)

data_service.delete_historical_game_data()

ui.print_game_end_message(datetime.now())

program_run_time = round(program_timer.stop(), 2)
ui.print_end_program_message(program_run_time)
