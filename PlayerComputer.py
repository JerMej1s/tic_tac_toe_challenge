import random

from typing import Optional

from Board import Board
from Game import PlayerSymbol
from Player import Player

CENTER_AND_CORNERS = ['1', '3', '5', '7', '9']

class PlayerComputer(Player):
    def get_move(self, board: Board) -> str:
        new_board: Board = board
        valid_moves: list[str] = new_board.get_valid_moves()

        def get_winning_move(symbol: PlayerSymbol) -> Optional[str]:
            winning_move: Optional[str] = None

            for valid_move in valid_moves:
                new_board.update_board(symbol, valid_move)
                
                is_game_over, _ = new_board.is_game_over()

                if is_game_over:
                    winning_move = valid_move
                    break
                else:
                    new_board.clear_cell(valid_move)
                    continue
            
            return winning_move

        # Try to win
        move: Optional[str] = get_winning_move(self.symbol)

        if move is None:
            # Block opponent's win
            opponent_symbol = (
                PlayerSymbol.O.value
                if self.symbol == PlayerSymbol.X.value
                else PlayerSymbol.X.value
            )
            move = get_winning_move(opponent_symbol)

        if move is None:
            # Choose a random corner or center
            valid_center_and_corners = [
                corner for corner in CENTER_AND_CORNERS
                if corner in valid_moves
            ]
            if valid_center_and_corners:
                move = str(random.choice(valid_center_and_corners))

        if move is None:
            # Choose a random move
            move = str(random.choice(valid_moves))

        return move
