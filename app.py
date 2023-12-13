from datetime import datetime

from Board import Board
from DataService import DataService
from Game import Game
from Player import PlayerSymbol
from PlayerComputer import PlayerComputer
from PlayerHuman import PlayerHuman
from Timer import Timer, TimeUnit
from UserInterface import ErrorMessage, UserInput, UserInterface

program_timer = Timer(TimeUnit.SECONDS)
program_timer.start()

ui = UserInterface()
player = PlayerHuman()
game_timer = Timer(TimeUnit.SECONDS)
data_warehouse = DataService()

is_playing = True

ui.print_game_start_message(datetime.now())

while is_playing:
    player = PlayerHuman()
    computer_player = PlayerComputer()
    game = Game()
    board = Board()
    is_first_turn = True
    is_game_over = False
    
    ui.play_with_computer()    

    if ui.is_computer_playing:
        computer_player = PlayerComputer()
        is_computer_first, computer_player.symbol = (
            ui.does_computer_go_first())

        if is_computer_first == None:
            is_playing = False
            break
        
        if is_computer_first:
            computer_move = computer_player.get_move(board.get_board())
            board.update_board(computer_move, computer_player.symbol)

        player.symbol = (PlayerSymbol.O.value
                         if computer_player.symbol == PlayerSymbol.X.value
                         else PlayerSymbol.X.value)
    elif ui.is_computer_playing is None:
        is_playing = False # User entered 'q' to quit
        break
    else:
        player.symbol = PlayerSymbol.X.value

    game_timer.start()

    while not is_game_over:
        if not is_first_turn:
            game.switch_player()

        player_move = None

        if  (ui.is_computer_playing # Non-human player's turn
             and game.current_player == computer_player.symbol):
            turn_timer = Timer(TimeUnit.MILLISECONDS)
            turn_timer.start()

            player_move = computer_player.get_move(board)
        else: # Human player's turn
            turn_timer = Timer(TimeUnit.SECONDS)
            probability_timer = Timer(TimeUnit.MILLISECONDS)
            turn_timer.start()
            probability_timer.start()
            
            win_probability = (round(
                board.get_win_probability(game.current_player) * 100, 2))
            probability_duration = probability_timer.stop()

            while True:
                ui.print_board_timestamp(board.updated_at)
                ui.print_board(board.board)
                ui.print_probability(game.current_player,
                                     win_probability, probability_duration)
                
                user_input = player.get_move(board)

                if user_input in board.get_valid_moves():
                    player_move = user_input
                    break
                elif user_input == UserInput.QUIT.value:
                    is_playing = False
                    break
                else:
                    print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                    continue
            
        if is_playing:
            board.update_board(player_move, game.current_player)

            is_game_over, game.winner = board.is_game_over()
            
            is_first_turn = False

            turn_duration = turn_timer.stop()
            game.tabulate_turn_duration(turn_duration)
        else:
            break

    if is_playing:
        game.duration = game_timer.stop()
        ui.print_board(board.board)
        game.print_winner()
        ui.print_game_details(game, board.updated_at, computer_player.symbol)
        data_warehouse.save_game_data(game)

        is_playing = ui.is_playing_again()

game_history = data_warehouse.get_historical_game_data()

if len(game_history) > 0:
    ui.print_historical_game_data(game_history)

data_warehouse.delete_historical_game_data()

ui.print_game_end_message(datetime.now())

program_run_time = program_timer.stop()
ui.print_end_program_message(program_run_time)