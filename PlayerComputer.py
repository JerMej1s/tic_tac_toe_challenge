import copy
import random

from typing import Optional

from Board import Board
from Game import PlayerSymbol
from Player import Player
from User import DifficultyLevel

CENTER_AND_CORNERS = ['1', '3', '5', '7', '9']

class PlayerComputer(Player):
    def __init__(self) -> None:
        self.difficulty_level: Optional[DifficultyLevel] = None

    def get_move(self, board: Board) -> str:
        new_board: Board = copy.deepcopy(board)
        valid_moves: list[str] = new_board.get_valid_moves()
        opponent_symbol = (
            PlayerSymbol.O.value
            if self.symbol == PlayerSymbol.X.value
            else PlayerSymbol.X.value
        )
        move: Optional[str] = None

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

        def minimax(
                move: str,
                is_maximizing: bool = True
            ) -> int:
            symbol: PlayerSymbol = (
                self.symbol
                if is_maximizing
                else opponent_symbol
            )
            new_board.update_board(symbol, move)
            
            game_over, _ = new_board.is_game_over()
            
            if game_over:
                return new_board.evaluate_score(self.symbol)
            else:
                return (max if is_maximizing else min)(
                    minimax(next_move, not is_maximizing)
                    for next_move in valid_moves
                )

        if self.difficulty_level != DifficultyLevel.EASY.value:
            # Try to win
            move = get_winning_move(self.symbol)

            if move is None:
                # Block opponent's win
                move = get_winning_move(opponent_symbol)

            if move is None:
                if (
                    self.difficulty_level == DifficultyLevel.MEDIUM.value
                    or len(valid_moves) == 9
                ):
                    # Choose a random corner or center
                    valid_center_and_corners = [
                        corner for corner in CENTER_AND_CORNERS
                        if corner in valid_moves
                    ]
                    if valid_center_and_corners:
                        move = str(random.choice(valid_center_and_corners))
                else:
                    # Use minimax algorithm to choose best move
                    move = max(valid_moves, key = minimax)

        if move is None:
            # Choose a random move
            move = str(random.choice(valid_moves))

        return move
