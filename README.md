# Tic Tac Toe

In this standard game of Tic Tac Toe, users can play in the console against another human player or against a computer player and choose between four difficulty levels: easy, medium, hard, and unbeatable.

### Motivation 🚸

This program was built for a coding challenge for a job interview.

## The Challenge 🧑‍💻

### Motivation 🚸

This coding challenge is intended to surface how engineering candidates approach problem-solving.

Special consideration will be granted to accuracy in meeting the requirements, performance of the code, code organization, robustness of the user experience, and duration for completing the challenge.

### Requirements ✅

In Python, make use of classes to build out tic-tac-toe with supplementary information. It will be standard rules. X always goes first. This will be done entirely in the console. The program starts by printing out the current time to the millisecond. Use ASCII art to build a board, with each box containing an X, O, or 1-9. Every time the board is displayed, it will be preceded by a timestamp (for validation purposes).

The user will input 1-9 to select which box to mark. It will inform the user whose turn it is (X or O). When the user is able to select input, a readout of all possible inputs will be displayed on the screen. The probability of winning (assuming players choose their options completely randomly) will be displayed, in addition to how long it took to calculate that number.

When the game finishes, it will say who won, how long each player took on their turn, and the total time spent in the game. They will then receive a prompt to either start a new game, or quit. Inputting “Q” always results in quitting.

Upon quitting, it displays:
  * the win percentage for X and O over the entire course of the program running
  * the duration of each game and who won
  * the total time spent by each player
  * the total time the program was running
  * it ends with a timestamp.

## Game Board 🔢

The game board is a `list` of nine elements, each representing a cell on the board. When the board is initialized, each element is set to a string representation of its corresponding cell number, 1-9. During play, the elements may be replaced with a player's symbol, `X` or `O`.

## Win Probability 🎲

During the game, on each human player's turn, the program estimates the probability that the current player will win the game based on the current state of the game board.
  * First, the program will generate a `set` of all possible permutations of the five Xs and four Os on the board.
    > 📢 Note: This set contains duplicate boards and invalid game boards, and thus, is significantly larger than a set containing all possible board outcomes, which impacts the accuracy of the calculated probability.
  * Next, the program will check whether each board is a valid future state of the current board.
    * A `zip()` function is used to iterate over each (non-empty) cell in the current board and the corresponding cell in each "possible" board at the same time. If the cells do not match, the board is eliminated as a possible end-state.
  * Of the remaining boards, the program will determine and count those which result in a win for the current player.
    * The program checks if any of the positions in a winning combination contain the current player's symbol. If they match, it means the player has a winning combination on the board.
    * The `set` of remaining boards is stored in memory to use on the next turn.
  * With the total number of possible remaining winning permutations and the total number of possible remaining end-state permutations, the estimated win probability is calculated and returned.

## Computer Player Strategy 💻

On the computer player's turn, the program will choose a move based on the difficulty level set by the user.

### Easy Mode

In easy mode, artificial intelligence is used to determine the worst move for the computer player based on the current state of the game board by considering each possible move and its possible outcome(s). It chooses the move that gives the human player the best opportunity to win.

### Medium Mode

In medium mode, the computer always chooses a move at random.

### Hard Mode

In hard mode, the computer player will choose a move based on the following prioritized criteria:
  * A move that results in an immeditate win for the computer player.
  * A move that blocks an opponent's win on their next turn.
  * A random available center or corner cell on the board.
  * A random available cell.

### Unbeatable Mode

In unbeatable mode, articifical intelligence is used to determine the best move based on the current state of the game board by considering each possible move and its possible outcome(s). This player will always win or draw, and thus it is unbeatable.
