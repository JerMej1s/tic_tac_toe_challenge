import os
import pickle

class DataWarehouse:
    def __init__(self):
        pass

    def save_game_data(self, game) -> None:
        game.possible_boards = None

        try:
            with open('game_history.pkl', 'ab') as f:
                pickle.dump(game, f)
        except:
            pass

    def get_historical_game_data(self) -> []:
        historical_game_data = []

        try:
            with open('game_history.pkl', 'rb') as f:
                while True:
                    try:
                        game = pickle.load(f)
                        historical_game_data.append(game)
                    except EOFError:
                        break
        except FileNotFoundError:
            return historical_game_data

        return historical_game_data

    def delete_historical_game_data(self) -> None:
        try:
            os.remove('game_history.pkl')
        except FileNotFoundError:
            pass
            
    def print_historical_game_data(self) -> None:
        game_history = self.get_historical_game_data()
        game_count = len(game_history)

        x_win_count = len(([game for game in game_history
                            if game.winner == 'X']))
        o_win_count = len(([game for game in game_history
                            if game.winner == 'O']))
        
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

        print(f"\nOut of {game_count} game(s), " +
              f"X won {x_win_percentage}% and " +
              f"O won {o_win_percentage}%. Congratulations!\n" +
              f"X took a total of {x_turn_duration} seconds to play and " +
              f"O took a total of {o_turn_duration} seconds to play.\n")
