# Tic Tac Toe

In this standard game of Tic Tac Toe, users can play in the console against a computer player or against another player.

🧠 An [AI player](#-artificial-intelligence-player-strategy) is currently under construction.

## 🚸 Motivation

I built this application for a coding challenge that was part of a job interview.

## 🧑‍💻 The Challenge

### 🚸 Motivation

This coding challenge is intended to surface how engineering candidates approach problem-solving.

Special consideration will be granted to accuracy in meeting the requirements, performance of the code, code organization, robustness of the user experience, and duration for completing the challenge.

### ✅ Acceptance Criteria

In Python, make use of classes to build out tic-tac-toe with supplementary information. It will be standard rules. X always goes first. This will be done entirely in the console. The program starts by printing out the current time to the millisecond. Use ASCII art to build a board, with each box containing an X, O, or 1-9. Every time the board is displayed, it will be preceded by a timestamp (for validation purposes).

The user will input 1-9 to select which box to mark. It will inform the user whose turn it is (X or O). When the user is able to select input, a readout of all possible inputs will be displayed on the screen. The probability of winning (assuming players choose their options completely randomly) will be displayed, in addition to how long it took to calculate that number.

When the game finishes, it will say who won, how long each player took on their turn, and the total time spent in the game. They will then receive a prompt to either start a new game, or quit. Inputting “Q” always results in quitting.

Upon quitting, it displays:
  ● the win percentage for X and O over the entire course of the program running
  ● the duration of each game and who won
  ● the total time spent by each player
  ● the total time the program was running
  ● it ends with a timestamp.

## 💻 Computer Player Strategy

On the computer's turn, the computer will choose a move based on the following prioritized criteria:
  * A move that results in an immeditate win for the computer player.
  * A move that blocks an opponent's win on their next turn.
  * A random available center or corner cell on the board.
  * A random available cell.

## 🧠 Artificial Intelligence Player Strategy

🚧 This player is under construction and not currently ready for game play. 🚧
