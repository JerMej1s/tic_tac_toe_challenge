from ComputerPlayer import ComputerPlayer
from DataWarehouse import DataWarehouse
from Game import Game
from Player import Player
from Timer import Timer, TimeUnit

program_timer = Timer(TimeUnit.SECONDS)
program_timer.start()

playing = True

while playing:
    player = Player()
    computer_player = ComputerPlayer()
    game = Game()
    data_warehouse = DataWarehouse()
    game_timer = Timer(TimeUnit.SECONDS)
    first_turn = True
    game_over = False
    
    game.start()

    is_computer_playing = computer_player.is_computer_playing()

    if is_computer_playing is None:
        playing = False # user entered 'q' to quit
        break

    if is_computer_playing:
        is_computer_first = computer_player.does_computer_go_first()

        if is_computer_first == None:
            playing = False
            break
        
        if is_computer_first:
            computer_move = computer_player.get_move(game.board)
            game.board.update_board(computer_move, computer_player.symbol)

        player.symbol = 'O' if computer_player.symbol == 'X' else 'X'
    else:
        player.symbol = 'X'

    game_timer.start()

    while not game_over:
        if not first_turn:
            game.switch_player()
            player.symbol = game.current_player

        if game.current_player == player.symbol:
            turn_timer = Timer(TimeUnit.SECONDS)
            turn_timer.start()
        elif game.current_player == computer_player.symbol:
            turn_timer = Timer(TimeUnit.MILLISECONDS)
            turn_timer.start()

        if  game.current_player == computer_player.symbol:
            computer_move = computer_player.get_move(game.board)
            game.board.update_board(computer_move, computer_player.symbol)
        else:
            game.board.print_board()
            game.board.print_probability(player.symbol)
        
            user_input = player.get_move(game.board)

            if user_input.lower() == 'q':
                playing = False
                break
        
            game.board.update_board(user_input, player.symbol)

            game_over, game.winner = game.board.is_game_over()
        
        first_turn = False

        turn_duration = turn_timer.stop()
        game.tabulate_turn_duration(turn_duration)

    if playing:
        game.duration = game_timer.stop()
        game.board.print_board()
        game.print_winner()
        game.print_game_details()
        data_warehouse.save_game_data(game)

        playing = game.do_play_again()

if playing:
    data_warehouse.print_historical_game_data()

#data_warehouse.delete_historical_game_data()

program_run_time = program_timer.stop()
print(f"\nProgram was running for {program_run_time} seconds.")

game.game_end()
