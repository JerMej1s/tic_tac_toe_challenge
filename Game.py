from enum import Enum

class PlayerSymbol(Enum):
    X = 'X'
    O = 'O'

class Game:
    def __init__(self) -> None:
        self.player_x_turn_duration = 0
        self.player_o_turn_duration = 0
        self.current_player = PlayerSymbol.X.value
        self.winner = None
        self.duration = None

    def switch_player(self) -> None:
        self.current_player = (PlayerSymbol.O.value
                               if self.current_player == PlayerSymbol.X.value
                               else PlayerSymbol.X.value)

    def tabulate_turn_duration(self, turn_duration: float) -> None:
        if self.current_player == PlayerSymbol.X.value:
            self.player_x_turn_duration += turn_duration
        else:
            self.player_o_turn_duration += turn_duration
