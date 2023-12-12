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
        print("\n")
        print("\n".join(["|".join(self.board[i:i+3])
                        for i in range(0, 9, 3)]))
        print("\n")

    def get_valid_moves(self) -> [str]:
        return [i for i in self.board if i not in ['X', 'O']]

    def is_game_over(self) -> (bool, str):
        for wc in WINNING_COMBINATIONS:
            if self.board[wc[0]] == self.board[wc[1]] == self.board[wc[2]]:
                winner = self.board[wc[0]]
                return True, winner
        
        if len(self.get_valid_moves()) == 0:
            return True, 'draw'
        
        return False, None 
