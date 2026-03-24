
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Players will guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Create Game Setup and Word Selection

#### Description
Set up the basic game structure where players can start a new Hangman game with a randomly selected word from a predefined list.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Initialize the game state (attempts remaining, guessed letters)
- Display the current progress of the word using underscores (_ _ _ format)
- Track incorrect guesses remaining


### 🛠️ Implement Player Input and Game Logic

#### Description
Create the main game loop that accepts letter guesses, updates game state, and manages win/lose conditions.

#### Requirements
Completed program should:

- Accept letter guesses from the player using `input()`
- Update the word progress when correct letters are guessed
- Track incorrect guesses and decrease attempts remaining
- End the game when the word is guessed (win condition)
- End the game when attempts are exhausted (lose condition)
- Display appropriate win/lose messages with the final word revealed
