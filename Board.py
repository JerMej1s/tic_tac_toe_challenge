import itertools

from datetime import datetime

# TODO: Remove duplicate boards and invalid boards.
ALL_BOARDS = set(itertools.permutations('XXXXXOOOO', 9))

WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
        self.possible_boards = set()
        self.updated_at = datetime.now()

    def get_board(self) -> [str]:
        return self.board
    
    def update_board(self, cell, player_symbol) -> None:
        self.board[int(cell) - 1] = player_symbol
        self.updated_at = datetime.now()

    def clear_cell(self, cell) -> None:
        cell_index = int(cell) - 1
        self.board[cell_index] = str(cell_index + 1)
        self.updated_at = datetime.now()

    def reset_board(self) -> None:
        self.board = [str(i) for i in range(1, 10)]
        self.updated_at = datetime.now()

    def get_valid_moves(self) -> [str]:
        return [i for i in self.board if i not in ['X', 'O']]

    def get_win_probability(self, player_symbol) -> float:
        num_wins = 0

        self.possible_boards = (set(board for board in ALL_BOARDS 
                                    if all(b == s for b, s
                                        in zip(board, self.board)
                                        if not s
                                        in map(str, range(1, 10)))))

        possible_wins = (set(board for board in self.possible_boards
                            if any(
                                board[wc[0]] == board[wc[1]] == board[wc[2]]
                                for wc in WINNING_COMBINATIONS)))

        for possible_win in possible_wins:
            if (any(possible_win[i] == player_symbol for wc
                    in WINNING_COMBINATIONS for i in wc)):
                num_wins += 1

        total_possible_boards = len(self.possible_boards)
        win_probability = (num_wins / total_possible_boards
                            if total_possible_boards else 0)

        return win_probability

    def is_game_over(self) -> (bool, str):
        for wc in WINNING_COMBINATIONS:
            if self.board[wc[0]] == self.board[wc[1]] == self.board[wc[2]]:
                winner = self.board[wc[0]]
                return True, winner
        
        if len(self.get_valid_moves()) == 0:
            return True, 'draw'
        
        return False, None 
