import pytest

from TicTacToe.src.Game import Game, PlayerSymbol

@pytest.fixture()
def game():
    yield Game()

def test_switch_player(game):
    assert game.current_player == PlayerSymbol.X
    
    game.switch_player()
    
    assert game.current_player == PlayerSymbol.O
    
    game.switch_player()
    
    assert game.current_player == PlayerSymbol.X

@pytest.mark.parametrize("current_player", [PlayerSymbol.X, PlayerSymbol.O])
@pytest.mark.parametrize("duration", [0, 0.375, 1, 2.5, 123456789])
def test_tabulate_turn_duration(game, current_player, duration):
    game.current_player = current_player

    assert game.player_x_turn_duration == 0
    assert game.player_o_turn_duration == 0
    
    game.tabulate_turn_duration(duration)
    
    assert game.player_x_turn_duration == (
        duration
        if current_player == PlayerSymbol.X
        else 0
    )
    assert game.player_o_turn_duration == (
        duration
        if current_player == PlayerSymbol.O
        else 0
    )

@pytest.mark.parametrize("duration", [-0.1, -1, -2.5, -123456789])
def test_tabulate_turn_duration_raises_when_negative_duration(game, duration):
    with pytest.raises(
        ValueError,
        match='Turn duration must be non-negative.'
    ):
        game.tabulate_turn_duration(duration)