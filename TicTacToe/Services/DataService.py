import os
import pickle

from TicTacToe.Game import Game

GAME_HISTORY_FILE = 'game_history.pkl'


class DataService:
    def __init__(self):
        pass

    def save_game_data(self, game: Game) -> None:
        try:
            with open(GAME_HISTORY_FILE, 'ab') as f:
                pickle.dump(game, f)
        except:
            pass

    def get_historical_game_data(self) -> list[Game]:
        historical_game_data: list[Game] = []

        try:
            with open(GAME_HISTORY_FILE, 'rb') as f:
                while True:
                    try:
                        game: Game = pickle.load(f)
                        historical_game_data.append(game)
                    except EOFError:
                        break
        except FileNotFoundError:
            pass

        return historical_game_data

    def delete_historical_game_data(self) -> None:
        try:
            os.remove(GAME_HISTORY_FILE)
        except FileNotFoundError:
            pass
