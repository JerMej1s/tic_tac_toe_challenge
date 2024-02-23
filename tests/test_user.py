import pytest
import sys

from io import StringIO

from TicTacToe.User import DifficultyLevel, User

@pytest.fixture()
def user():
    yield User()


class TestUser:
    @pytest.mark.parametrize("user_input", ['y', "Y"])
    def test_is_computer_playing_returns_true(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.is_computer_playing()

        assert result is True

    @pytest.mark.parametrize("user_input", ['n', "N"])
    def test_is_computer_playing_returns_false(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.is_computer_playing()

        assert result is False

    @pytest.mark.parametrize("user_input", ['q', "Q"])
    def test_is_computer_playing_returns_none(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.is_computer_playing()

        assert result is None

    @pytest.mark.parametrize(
        "user_input",
        [
            'yes', 'Yes', 'YES',
            'no', 'No', 'NO',
            'quit', 'Quit', 'QUIT',
            'abc123', '1234567890', '1n\/@Lid_|npU7'
        ]
    )
    def test_is_computer_playing_prompts_user_again(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        responses = iter([user_input, 'q'])
        def mock_input(_) -> str:
            return next(responses)
        monkeypatch.setattr('builtins.input', mock_input)
        actual_output = StringIO()
        monkeypatch.setattr(sys, 'stdout', actual_output)
        expected_output = 'Invalid input. Please try again.'

        result = user.is_computer_playing()

        assert result is None
        assert expected_output in actual_output.getvalue()

    @pytest.mark.parametrize("user_input", ['y', "Y"])
    def test_does_computer_go_first_returns_false(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.does_computer_go_first()

        assert result is False

    @pytest.mark.parametrize("user_input", ['n', "N"])
    def test_does_computer_go_first_returns_true(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.does_computer_go_first()

        assert result is True

    @pytest.mark.parametrize("user_input", ['q', "Q"])
    def test_does_computer_go_first_returns_none(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.does_computer_go_first()

        assert result is None

    @pytest.mark.parametrize(
        "user_input",
        [
            'yes', 'Yes', 'YES',
            'no', 'No', 'NO',
            'quit', 'Quit', 'QUIT',
            'abc123', '1234567890', '1n\/@Lid_|npU7'
        ]
    )
    def test_does_computer_go_first_prompts_user_again(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        responses = iter([user_input, 'q'])
        def mock_input(_) -> str:
            return next(responses)
        monkeypatch.setattr('builtins.input', mock_input)
        actual_output = StringIO()
        monkeypatch.setattr(sys, 'stdout', actual_output)
        expected_output = 'Invalid input. Please try again.'

        result = user.does_computer_go_first()

        assert result is None
        assert expected_output in actual_output.getvalue()

    def test_get_difficulty_level_returns_easy(
            self,
            user: User,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return '1'
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.get_difficulty_level()

        assert result == DifficultyLevel.EASY

    def test_get_difficulty_level_returns_medium(
            self,
            user: User,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return '2'
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.get_difficulty_level()

        assert result == DifficultyLevel.MEDIUM

    def test_get_difficulty_level_returns_hard(
            self,
            user: User,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return '3'
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.get_difficulty_level()

        assert result == DifficultyLevel.HARD

    def test_get_difficulty_level_returns_unbeatable(
            self,
            user: User,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return '4'
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.get_difficulty_level()

        assert result == DifficultyLevel.UNBEATABLE

    @pytest.mark.parametrize("user_input", ['q', "Q"])
    def test_get_difficulty_level_returns_none(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.get_difficulty_level()

        assert result is None

    @pytest.mark.parametrize(
        "user_input",
        [
            '5', '6', '7', '8', '9', '10',
            'abc123', '1234567890', '1n\/@Lid_|npU7'
        ]
    )
    def test_get_difficulty_level_prompts_user_again(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        responses = iter([user_input, 'q'])
        def mock_input(_) -> str:
            return next(responses)
        monkeypatch.setattr('builtins.input', mock_input)
        actual_output = StringIO()
        monkeypatch.setattr(sys, 'stdout', actual_output)
        expected_output = 'Invalid input. Please try again.'

        result = user.get_difficulty_level()

        assert result is None
        assert expected_output in actual_output.getvalue()

    @pytest.mark.parametrize("user_input", ['y', "Y"])
    def test_is_playing_again_returns_true(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.is_playing_again()

        assert result is True

    @pytest.mark.parametrize("user_input", ['n', "N", 'q', "Q"])
    def test_is_playing_again_returns_false(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        def mock_input(_) -> str:
            return user_input
        monkeypatch.setattr('builtins.input', mock_input)

        result = user.is_playing_again()

        assert result is False

    @pytest.mark.parametrize(
        "user_input",
        [
            'yes', 'Yes', 'YES',
            'no', 'No', 'NO',
            'quit', 'Quit', 'QUIT',
            'abc123', '1234567890', '1n\/@Lid_|npU7'
        ]
    )
    def test_is_playing_again_prompts_user_again(
            self,
            user: User,
            user_input: str,
            monkeypatch: pytest.MonkeyPatch
        ):
        responses = iter([user_input, 'q'])
        def mock_input(_) -> str:
            return next(responses)
        monkeypatch.setattr('builtins.input', mock_input)
        actual_output = StringIO()
        monkeypatch.setattr(sys, 'stdout', actual_output)
        expected_output = 'Invalid input. Please try again.'

        result = user.is_playing_again()

        assert result is False
        assert expected_output in actual_output.getvalue()
