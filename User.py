from enum import Enum
from typing import Optional

class ErrorMessage(Enum):
    INVALID_INPUT = "Invalid input. Please try again."

class UserInput(Enum):
    YES = 'y'
    NO = 'n'
    QUIT = 'q'

class User:
    def __init__(self) -> None:
        pass

    def is_computer_playing(self) -> Optional[bool]:
        while True:
            user_input = input("\nDo you want to play against the computer?" +
                               " [y/n or q to quit]: ").lower()
            
            if user_input == UserInput.YES.value:
                return True
            elif user_input == UserInput.NO.value:
                return False
            elif user_input == UserInput.QUIT.value:
                return None
            else:
                print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                continue
    
    def does_computer_go_first(self) -> (Optional[bool]):
        while True:
            user_input = input("\nDo you want to go first? " +
                                "[y/n or q to quit]: ").lower()
            
            if user_input == UserInput.YES.value:
                return False 
            elif user_input == UserInput.NO.value:
                return True
            elif user_input == UserInput.QUIT.value:
                return None
            else:
                print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                continue

    def is_playing_again(self) -> bool:
        while True:
            user_input = (input("\nDo you want to play again? [y/n/q]: ")
                            .lower())
            
            if (user_input == UserInput.NO.value
                or user_input == UserInput.QUIT.value):
                return False
            elif user_input == UserInput.YES.value:
                return True
            else:
                print(f"\n{ErrorMessage.INVALID_INPUT.value}")
                continue
