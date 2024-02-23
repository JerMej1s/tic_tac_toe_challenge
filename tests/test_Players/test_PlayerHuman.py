from io import StringIO

import pytest
import sys

from TicTacToe.Board import Board
from TicTacToe.Game import PlayerSymbol
from TicTacToe.Players.PlayerHuman import PlayerHuman

@pytest.fixture()
def player_human():
    yield PlayerHuman(symbol=PlayerSymbol.X)

@pytest.fixture()
def board():
    yield Board()


class TestPlayerHuman:
    @pytest.mark.parametrize("user_input", range(1, 10))
    def test_get_move_returns_user_input(
            self,
            player_human: PlayerHuman,
            board: Board,
            user_input: int,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return str(user_input)
        monkeypatch.setattr('builtins.input', mock_input)
        expected_move = str(user_input)

        actual_move = player_human.get_move(board)

        assert actual_move == expected_move

    @pytest.mark.parametrize("user_input", ['q', 'Q'])
    def test_get_move_returns_none(
            self,
            player_human: PlayerHuman,
            board: Board,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        actual_move = player_human.get_move(board)

        assert actual_move == None

    @pytest.mark.parametrize(
        "user_input",
        [
            'one', 'Two', 'THREE',
            'y', 'Y', 'yes',
            'n', 'N', 'no',
            'abc123', '1234567890', '1n\/@Lid_|npU7'
        ]
    )
    def test_get_move_prompts_user_again(
            self,
            player_human: PlayerHuman,
            board: Board,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        player_human: PlayerHuman = PlayerHuman(symbol=PlayerSymbol.X)
        responses = iter([user_input, 'q'])
        def mock_input(_) -> str:
            return next(responses)
        monkeypatch.setattr('builtins.input', mock_input)
        actual_output = StringIO()
        monkeypatch.setattr(sys, 'stdout', actual_output)
        expected_output = 'Invalid input. Please try again.'

        actual_move = player_human.get_move(board)

        assert actual_move == None
        assert expected_output in actual_output.getvalue()
