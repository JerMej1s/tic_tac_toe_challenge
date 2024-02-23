import random
import pytest

from TicTacToe.Board import Board
from TicTacToe.Game import PlayerSymbol
from TicTacToe.Players.PlayerComputer import PlayerComputer
from TicTacToe.User import DifficultyLevel


class TestPlayerComputer:
    @pytest.mark.parametrize("difficulty_level", [
        DifficultyLevel.EASY,
        DifficultyLevel.MEDIUM,
        DifficultyLevel.HARD,
        DifficultyLevel.UNBEATABLE
    ])
    @pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
    def test_get_move_raises_value_error(
            self,
            difficulty_level: DifficultyLevel,
            player_symbol: PlayerSymbol
        ):
        player: PlayerComputer = PlayerComputer(
            difficulty_level=difficulty_level,
            symbol=player_symbol
        )
        board: Board = Board()
        cells = [str(i) for i in range(1, 10)]
        for _ in range(9):
            cell = random.choice(cells)
            cells.remove(cell)
            board.update_board(player_symbol, cell)
            player_symbol = (
                PlayerSymbol.X
                if player_symbol == PlayerSymbol.O
                else PlayerSymbol.O
            )

        with pytest.raises(ValueError) as error:
            player.get_move(board)

        assert str(error.value) == 'No valid moves available.'
