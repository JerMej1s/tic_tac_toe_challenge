from Player import PlayerSymbol

class Game:
    def __init__(self) -> None:
        self.player_x_turn_duration = 0
        self.player_o_turn_duration = 0
        self.current_player = PlayerSymbol.X.value
        self.winner = None
        self.duration = None

    def switch_player(self,) -> None:
        self.current_player = (PlayerSymbol.O.value
                               if self.current_player == PlayerSymbol.X.value
                               else PlayerSymbol.X.value)

    def tabulate_turn_duration(self, turn_duration) -> None:
        if self.current_player == PlayerSymbol.X.value:
            self.player_x_turn_duration += turn_duration
        else:
            self.player_o_turn_duration += turn_duration

    def print_winner(self) -> None:
        if self.winner == None:
            return
        elif self.winner == 'draw':
            print("It's a draw!\n")
        else:
            print(f"Player {self.winner} wins!\n")
