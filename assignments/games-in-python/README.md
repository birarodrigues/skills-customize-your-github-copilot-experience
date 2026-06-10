
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python where the player guesses letters to reveal a hidden word. In this assignment, you will practice string manipulation, loops, conditionals, and random word selection.

## 📝 Tasks

### 🛠️	Implement the Core Hangman Game Loop

#### Description
Create a program that selects a random word from a predefined list and runs a game loop where the player guesses one letter at a time until they win or run out of attempts.

#### Requirements
Completed program should:

- Define a list with at least 5 possible words and randomly select one at the start of the game.
- Display the current progress using underscores for unknown letters (example: `_ _ _ _ _`).
- Accept one letter guess per turn from user input.
- Reveal all matching positions when a guessed letter exists in the word.
- Track and display the number of incorrect guesses remaining.
- End the game with a win message when all letters are revealed.
- End the game with a lose message when attempts reach 0, showing the correct word.


### 🛠️	Validate Input and Improve Player Feedback

#### Description
Enhance the game experience by handling invalid or repeated guesses and by displaying clear feedback after each turn.

#### Requirements
Completed program should:

- Reject invalid inputs (empty input, more than one character, non-letter characters) and ask the player to try again.
- Track previously guessed letters and notify the player when a letter has already been used.
- Display guessed letters each round so the player can see their history.
- Show clear status messages for correct and incorrect guesses.
- Keep game output readable and organized across turns.
