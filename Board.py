import itertools

from datetime import datetime
from Timer import Timer, TimeUnit

# TODO: Remove duplicate boards and invalid boards.
ALL_BOARDS = set(itertools.permutations('XXXXXOOOO', 9))

WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        self.possible_boards = []

    def update_board(self, cell, player_symbol) -> None:
        self.board[int(cell) - 1] = player_symbol

    def clear_cell(self, cell) -> None:
        cell_index = int(cell) - 1
        self.board[cell_index] = str(cell_index + 1)

    def print_board(self) -> None:
            # Print timestamp
            print("\n")
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

            # Print current game board
            print("\n")
            print("\n".join(["|".join(self.board[i:i+3])
                            for i in range(0, 9, 3)]))
            print("\n")

    def get_valid_moves(self) -> [str]:
        return [i for i in self.board if i not in ['X', 'O']]


    def get_win_probability(self, player_symbol) -> (float, float):
        execution_timer = Timer(TimeUnit.MILLISECONDS)
        execution_timer.start()

        num_wins = 0

        if not self.possible_boards:
            self.possible_boards = ([board for board in ALL_BOARDS 
                                     if all(b == s for b, s
                                            in zip(board, self.board)
                                            if not s
                                            in map(str, range(1, 10)))])

        possible_wins = ([board for board in self.possible_boards
                          if any(board[wc[0]] == board[wc[1]] == board[wc[2]]
                                 for wc in WINNING_COMBINATIONS)])

        for possible_win in possible_wins:
            if (any(possible_win[i] == player_symbol for wc
                    in WINNING_COMBINATIONS for i in wc)):
                num_wins += 1

        total_possible_boards = len(self.possible_boards)
        win_probability = (num_wins / total_possible_boards
                           if total_possible_boards else 0)

        execution_duration = execution_timer.stop()

        return win_probability, execution_duration

    def print_probability(self, player_symbol) -> None:
        result = self.get_win_probability(player_symbol)
        win_probability = round(result[0] * 100, 2)
        processing_time = result[1]

        print(f"Player {player_symbol} has a " +
                f"{win_probability}% chance of winning, " +
                f"which took {processing_time} milliseconds to calculate.")

    def is_game_over(self) -> (bool, str):
        for wc in WINNING_COMBINATIONS:
            if self.board[wc[0]] == self.board[wc[1]] == self.board[wc[2]]:
                winner = self.board[wc[0]]
                return True, winner
        
        if len(self.get_valid_moves()) == 0:
            return True, 'draw'
        
        return False, None 
