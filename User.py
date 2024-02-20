from enum import Enum
from typing import Optional

class DifficultyLevel(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    UNBEATABLE = 'unbeatable'

class ErrorMessage(Enum):
    INVALID_INPUT = "Invalid input. Please try again."

class UserInput(Enum):
    YES = 'y'
    NO = 'n'
    QUIT = 'q'
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'

YES_NO_QUIT_INPUT_OPTIONS = (
    f"[{UserInput.YES.value}/{UserInput.NO.value} or " +
    f"{UserInput.QUIT.value} to {UserInput.QUIT.name.lower()}]"
)

class User:
    def __init__(self) -> None:
        pass

    def is_computer_playing(self) -> Optional[bool]:
        while True:
            user_input: str = input(
                "\nDo you want to play against the computer? " +
                f"{YES_NO_QUIT_INPUT_OPTIONS}: "
            ).lower()
            
            if user_input == UserInput.YES.value:
                return True
            elif user_input == UserInput.NO.value:
                return False
            elif user_input == UserInput.QUIT.value:
                return None
            else:
                print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                continue

    def does_computer_go_first(self) -> Optional[bool]:
        while True:
            user_input: str = input(
                f"\nDo you want to go first? {YES_NO_QUIT_INPUT_OPTIONS}: "
            ).lower()
            
            if user_input == UserInput.YES.value:
                return False 
            elif user_input == UserInput.NO.value:
                return True
            elif user_input == UserInput.QUIT.value:
                return None
            else:
                print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                continue

    def get_difficulty_level(self) -> Optional[DifficultyLevel]:
        while True:
            user_input: str = input(
                f"\nChoose a difficulty level: " +
                f"Enter {UserInput.ONE.value} for " +
                f"{DifficultyLevel.EASY.value}, " +
                f"{UserInput.TWO.value} for " +
                f"{DifficultyLevel.MEDIUM.value}, " +
                f"{UserInput.THREE.value} for "+
                f"{DifficultyLevel.HARD.value}, " +
                f"{UserInput.FOUR.value} for " +
                f"{DifficultyLevel.UNBEATABLE.value}, or " +
                f"{UserInput.QUIT.value} to " +
                f"{UserInput.QUIT.name.lower()}: "
            ).lower()
            
            if  user_input == UserInput.ONE.value:
                return DifficultyLevel.EASY
            elif user_input == UserInput.TWO.value:
                return DifficultyLevel.MEDIUM
            elif user_input == UserInput.THREE.value:
                return DifficultyLevel.HARD
            elif user_input == UserInput.FOUR.value:
                return DifficultyLevel.UNBEATABLE
            elif user_input == UserInput.QUIT.value:
                return None
            else:
                print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                continue

    def is_playing_again(self) -> bool:
        while True:
            user_input: str = input(
                f"\nDo you want to play again? {YES_NO_QUIT_INPUT_OPTIONS}: "
            ).lower()
            
            if user_input == UserInput.YES.value:
                return True
            elif (
                user_input == UserInput.NO.value
                or user_input == UserInput.QUIT.value
            ):
                return False
            else:
                print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                continue
