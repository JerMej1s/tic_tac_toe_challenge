import itertools

from Board import WINNING_COMBINATIONS
from Timer import Timer, TimeUnit

# TODO: Remove duplicate boards and invalid boards.
ALL_BOARDS = set(itertools.permutations('XXXXXOOOO', 9))

class Probability():
    def __init__(self) -> None:
        pass
    
    def get_win_probability(self, game_board, player_symbol) -> (float, float):
        execution_timer = Timer(TimeUnit.MILLISECONDS)
        execution_timer.start()

        num_wins = 0

        self.possible_boards = ([board for board in ALL_BOARDS 
                                    if all(b == s for b, s
                                        in zip(board, game_board.board)
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

    def print_probability(self, game) -> None:
        result = self.get_win_probability(game.board, game.current_player)
        win_probability = round(result[0] * 100, 2)
        processing_time = result[1]

        print(f"Player {game.current_player} has a " +
                f"{win_probability}% chance of winning, " +
                f"which took {processing_time} milliseconds to calculate.")
        