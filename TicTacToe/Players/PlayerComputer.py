import copy
import math
import random
from typing import Optional

from TicTacToe.Board import Board
from TicTacToe.Game import PlayerSymbol
from TicTacToe.Players.Player import Player
from TicTacToe.User import DifficultyLevel

CENTER_AND_CORNERS = ['1', '3', '5', '7', '9']


class PlayerComputer(Player):
    def __init__(self, symbol: PlayerSymbol, difficulty_level=None) -> None:
        super().__init__(symbol=symbol)
        self.difficulty_level: Optional[DifficultyLevel] = difficulty_level

    def get_move(self, board: Board) -> str:
        new_board: Board = copy.deepcopy(board)
        valid_moves: list[str] = new_board.get_valid_moves()

        if not valid_moves:
            raise ValueError('No valid moves available.')

        opponent_symbol: PlayerSymbol = PlayerSymbol.O \
            if self.symbol == PlayerSymbol.X else PlayerSymbol.X

        def minimax(
                board: Board,
                depth: int = 0,
                is_maximizing: bool = True
            ) -> int:
            game_over, _ = board.is_game_over()

            if game_over:
                return board.evaluate_score(symbol=self.symbol)

            bestScore = -math.inf if is_maximizing else math.inf
            score_update = max if is_maximizing else min
            symbol: PlayerSymbol = (self.symbol
                if is_maximizing else opponent_symbol
            )

            for valid_move in board.get_valid_moves():
                new_board.update_board(
                    player_symbol=symbol,
                    cell=valid_move
                )
                score = minimax(
                    board=new_board,
                    depth=depth + 1,
                    is_maximizing=not is_maximizing
                )
                new_board.clear_cell(cell=valid_move)
                bestScore = score_update(score, bestScore)
            return bestScore

        def get_winning_move(symbol: PlayerSymbol) -> Optional[str]:
            winning_move: Optional[str] = None

            for valid_move in valid_moves:
                new_board.update_board(player_symbol=symbol, cell=valid_move)
                is_game_over, _ = new_board.is_game_over()
                if is_game_over:
                    winning_move = valid_move
                    break
                else:
                    new_board.clear_cell(cell=valid_move)

            return winning_move

        move: Optional[str] = None

        if (self.difficulty_level == DifficultyLevel.UNBEATABLE
            and len(valid_moves) < 9
        ):
            # Use minimax algorithm to choose best move
            best_score: float = -math.inf
            best_moves: list[str] = []
            score: float = best_score

            for valid_move in valid_moves:
                new_board.update_board(
                    player_symbol=self.symbol,
                    cell=valid_move
                )
                score = minimax(board=new_board, depth=0, is_maximizing=False)
                new_board.clear_cell(cell=valid_move)
                if score > best_score:
                    best_score = score
                    best_moves = [valid_move]
                elif score == best_score:
                    best_moves.append(valid_move)
            if best_moves:
                move = str(random.choice(best_moves))
        elif self.difficulty_level == DifficultyLevel.HARD:
            # Try to win or block opponent's win
            move = get_winning_move(symbol=self.symbol) \
                or get_winning_move(symbol=opponent_symbol)
            if move is None:
                # Choose a random corner or center
                valid_center_and_corners = [
                    cc for cc in CENTER_AND_CORNERS
                    if cc in valid_moves
                ]
                if valid_center_and_corners:
                    move = str(random.choice(valid_center_and_corners))
        elif self.difficulty_level == DifficultyLevel.EASY:
            # Use minimax algorithm to choose worst move
            worst_score: float = math.inf
            worst_moves: list[str] = []
            score: float = worst_score

            for valid_move in valid_moves:
                new_board.update_board(
                    player_symbol=self.symbol,
                    cell=valid_move
                )
                score = minimax(board=new_board, depth=0, is_maximizing=False)
                new_board.clear_cell(cell=valid_move)
                if score < worst_score:
                    worst_score = score
                    worst_moves = [valid_move]
                elif score == worst_score:
                    worst_moves.append(valid_move)
            if worst_moves:
                move = str(random.choice(worst_moves))

        if move is None:
            # Choose a random move
            move = str(random.choice(valid_moves))

        return move
