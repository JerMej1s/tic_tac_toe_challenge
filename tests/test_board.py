import pytest
import random

from datetime import datetime

from TicTacToe.src.Board import Board, WINNING_COMBINATIONS
from TicTacToe.src.Game import PlayerSymbol

@pytest.fixture()
def board():
    yield Board()

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("cell", [str(i) for i in range(1, 10)])
def test_update_board_correctly(
    board,
    player_symbol: PlayerSymbol,
    cell: str
):
    before = datetime.now()
    board.update_board(player_symbol, cell)
    after = datetime.now()

    assert board.board[int(cell) - 1] == player_symbol
    assert before <= board.updated_at <= after

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize(
    "cell",
    [str(i) for i in set(range(-10, 20)) - set(range(1, 10))]
)
def test_update_board_raises_when_invalid_cell(board, player_symbol, cell):
    with pytest.raises(ValueError, match='Invalid cell.'):
        board.update_board(player_symbol, cell)

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("cell", [str(i) for i in range(1, 10)])
def test_update_board_raises_when_cell_filled(
    board,
    player_symbol: PlayerSymbol,
    cell: str
):
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

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("cell", [str(i) for i in range(1, 10)])
def test_clear_cell_correctly(board, player_symbol, cell):
    board.update_board(player_symbol, cell)
    
    before = datetime.now()
    board.clear_cell(cell)
    after = datetime.now()

    assert board.board[int(cell) - 1] == cell
    assert before <= board.updated_at <= after

@pytest.mark.parametrize(
    "cell",
    [str(i) for i in set(range(-10, 20)) - set(range(1, 10))]
)
def test_clear_cell_raises_when_invalid_cell(board, cell):
    with pytest.raises(ValueError, match='Invalid cell.'):
        board.clear_cell(cell)

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("num_turns", range(1, 10))
def test_reset_board(board, player_symbol, num_turns):
    cells = [str(i) for i in range(1, 10)]
    for _ in range(num_turns):
        cell = random.choice(cells)
        cells.remove(cell)
        board.update_board(player_symbol, cell)
        player_symbol = (
            PlayerSymbol.X
            if player_symbol == PlayerSymbol.O
            else PlayerSymbol.O
        )

    before = datetime.now()
    board.reset_board()
    after = datetime.now()

    assert board.board == [str(i) for i in range(1, 10)]
    assert before <= board.updated_at <= after

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("num_turns", range(1, 10))
def test_get_valid_moves(board, player_symbol, num_turns):
    cells = [str(i) for i in range(1, 10)]
    for _ in range(num_turns):
        cell = random.choice(cells)
        cells.remove(cell)
        board.update_board(player_symbol, cell)
        player_symbol = (
            PlayerSymbol.X
            if player_symbol == PlayerSymbol.O
            else PlayerSymbol.O
        )

    assert board.get_valid_moves() == cells

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("wc", WINNING_COMBINATIONS)
def test_is_game_over_returns_winner(board, player_symbol, wc):
    for index in wc:
        cell = str(index + 1)
        board.update_board(player_symbol, cell)

    assert board.is_game_over() == (True, player_symbol)

@pytest.mark.parametrize(
        "draw_board",
        [
            ['X', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'O'],
            ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'O'],
            ['X', 'O', 'O', 'O', 'X', 'X', 'O', 'X', 'O']
        ]
    )
def test_is_game_over_returns_draw(board, draw_board):
    for i in range(9):
        if draw_board[i] == PlayerSymbol.X.value:
            player_symbol = PlayerSymbol.X
        else:
            player_symbol = PlayerSymbol.O
        cell = str(i + 1)
        board.update_board(player_symbol, cell)

    assert board.is_game_over() == (True, 'draw')

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
def test_is_game_over_returns_false(board, player_symbol):
    cells = [str(i) for i in range(1, 10)]
    for _ in range(4):
        cell = random.choice(cells)
        cells.remove(cell)
        board.update_board(player_symbol, cell)
        player_symbol = (
            PlayerSymbol.X
            if player_symbol == PlayerSymbol.O
            else PlayerSymbol.O
        )
    
    assert board.is_game_over() == (False, None)

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("wc", WINNING_COMBINATIONS)
def test_evaluate_score_returns_1_and_neg1(board, player_symbol, wc):
    for index in wc:
        cell = str(index + 1)
        board.update_board(player_symbol, cell)

    assert board.evaluate_score(player_symbol) == 1

    opponent_symbol = (
        PlayerSymbol.X
        if player_symbol == PlayerSymbol.O
        else PlayerSymbol.O
    )

    assert board.evaluate_score(opponent_symbol) == -1

@pytest.mark.parametrize(
        "draw_board",
        [
            ['X', 'O', 'X', 'O', 'O', 'X', 'O', 'X', 'O'],
            ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'O'],
            ['X', 'O', 'O', 'O', 'X', 'X', 'O', 'X', 'O']
        ]
    )
def test_evaluate_score_returns_0(board, draw_board):
    for i in range(9):
        if draw_board[i] == PlayerSymbol.X.value:
            player_symbol = PlayerSymbol.X
        else:
            player_symbol = PlayerSymbol.O
        cell = str(i + 1)
        board.update_board(player_symbol, cell)
    
    assert board.evaluate_score(player_symbol) == 0

@pytest.mark.parametrize("player_symbol", [PlayerSymbol.X, PlayerSymbol.O])
def test_evaluate_score_raises_when_game_not_over(board, player_symbol):
    cells = [str(i) for i in range(1, 10)]
    for _ in range(4):
        cell = random.choice(cells)
        cells.remove(cell)
        board.update_board(player_symbol, cell)
        player_symbol = (
            PlayerSymbol.X
            if player_symbol == PlayerSymbol.O
            else PlayerSymbol.O
        )

    with pytest.raises(ValueError, match='Game is not over.'):
        board.evaluate_score(player_symbol)