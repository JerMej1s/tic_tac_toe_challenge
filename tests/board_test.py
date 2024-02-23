import pytest

from datetime import datetime

from TicTacToe.src.Board import Board
from TicTacToe.src.Game import PlayerSymbol

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("cell", [str(i) for i in range(1, 10)])
def test_update_board_correctly(player_symbol: PlayerSymbol, cell: str):
    board = Board()
    before = datetime.now()
    board.update_board(player_symbol, cell)
    after = datetime.now()

    assert board.board[int(cell) - 1] == player_symbol
    assert before <= board.updated_at <= after

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("cell", [str(i) for i in range(1, 10)])
def test_update_board_raises_error(player_symbol: PlayerSymbol, cell: str):
    board = Board()
    board.update_board(player_symbol, cell)
    opponent_symbol = (
        PlayerSymbol.X
        if player_symbol == PlayerSymbol.O
        else PlayerSymbol.O
    )

    with pytest.raises(
        ValueError,
        match=f'Cell {cell} is already filled with {player_symbol}.'
    ):
        board.update_board(opponent_symbol, cell)