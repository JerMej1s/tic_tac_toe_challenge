from PlayerComputer import PLayerComputer
from DataService import DataWarehouse
from Game import Game
from PlayerHuman import PlayerHuman
from PlayerSymbol import PlayerSymbol
from Timer import Timer, TimeUnit
from UserInput import UserInput
from UserInterface import UserInterface

program_timer = Timer(TimeUnit.SECONDS)
program_timer.start()
ui = UserInterface()

playing = True

while playing:
    player = PlayerHuman()
    computer_player = PLayerComputer()
    game = Game()
    data_warehouse = DataWarehouse()
    game_timer = Timer(TimeUnit.SECONDS)
    first_turn = True
    game_over = False
    
    game.start()

    ui.play_with_computer()

    if ui.is_computer_playing is None:
        playing = False # User entered 'q' to quit
        break

    if ui.is_computer_playing:
        is_computer_first, computer_player.symbol = (
            ui.does_computer_go_first())

        if is_computer_first == None:
            playing = False
            break
        
        if is_computer_first:
            computer_move = computer_player.get_move(game.board)
            game.board.update_board(computer_move, computer_player.symbol)

        player.symbol = (PlayerSymbol.O.value
                         if computer_player.symbol == PlayerSymbol.X.value
                         else PlayerSymbol.X.value)
    else:
        player.symbol = PlayerSymbol.X.value

    game_timer.start()

    while not game_over:
        if not first_turn:
            game.switch_player()

        if (ui.is_computer_playing
            and game.current_player == computer_player.symbol):
            turn_timer = Timer(TimeUnit.MILLISECONDS)
            turn_timer.start()
        else:
            turn_timer = Timer(TimeUnit.SECONDS)
            turn_timer.start()

        if  (ui.is_computer_playing
             and game.current_player == computer_player.symbol):
            computer_move = computer_player.get_move(game.board)
            game.board.update_board(computer_move, computer_player.symbol)
        else:
            game.board.print_board()
            game.board.print_probability(game.current_player)
        
            user_input = player.get_move(game)

            if user_input.lower() == UserInput.QUIT.value:
                playing = False
                break
        
            game.board.update_board(user_input, game.current_player)

        game_over, game.winner = game.board.is_game_over()
        
        first_turn = False

        turn_duration = turn_timer.stop()
        game.tabulate_turn_duration(turn_duration)

    if playing:
        game.duration = game_timer.stop()
        game.board.print_board()
        game.print_winner()
        ui.print_game_details(game, computer_player.symbol)
        data_warehouse.save_game_data(game)

        playing = ui.is_playing_again()

game_history = data_warehouse.get_historical_game_data()

if len(game_history) > 0:
    ui.print_historical_game_data(game_history)

#data_warehouse.delete_historical_game_data()

program_run_time = program_timer.stop()
print(f"\nProgram was running for {program_run_time} seconds.")

game.game_end()
