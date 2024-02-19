import copy
import math
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

        def minimax(
                board: Board,
                depth: int = 0,
                is_maximizing: bool = True
            ) -> int:
            game_over, _ = board.is_game_over()
            
            if game_over:
                return board.evaluate_score(self.symbol)
            
            bestScore = -math.inf if is_maximizing else math.inf
            score_update = max if is_maximizing else min
            symbol = self.symbol if is_maximizing else opponent_symbol

            for valid_move in board.get_valid_moves():
                new_board.update_board(symbol, valid_move)
                score = minimax(new_board, depth + 1, not is_maximizing)
                bestScore = score_update(score, bestScore)
                new_board.clear_cell(valid_move)
            return bestScore
        
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
        
        if self.difficulty_level == DifficultyLevel.HARD:
            # Use minimax algorithm to choose best move
            bestScore: float = -math.inf
            score: float = bestScore

            for valid_move in valid_moves:
                new_board.update_board(self.symbol, valid_move)
                score = minimax(new_board, 0, False)
                new_board.clear_cell(valid_move)
                if score > bestScore:
                    bestScore = score
                    move = valid_move
        elif self.difficulty_level == DifficultyLevel.MEDIUM:
            # Try to win or block opponent's win
            move = (
                get_winning_move(self.symbol)
                or get_winning_move(opponent_symbol)
            )

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
