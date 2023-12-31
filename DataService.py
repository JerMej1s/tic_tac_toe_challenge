import os
import pickle

from Game import Game

class DataService:
    def __init__(self):
        pass

    def save_game_data(self, game: Game) -> None:
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
            pass

        return historical_game_data

    def delete_historical_game_data(self) -> None:
        try:
            os.remove('game_history.pkl')
        except FileNotFoundError:
            pass
