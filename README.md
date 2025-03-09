# Hangman Game

## Description
Hangman is a word-guessing game where players try to guess a hidden word by suggesting letters within a limited number of attempts. This Python implementation of Hangman provides an interactive console-based experience.

## Features
- Random word selection
- Player can guess letters one at a time
- Limited number of incorrect guesses
- ASCII Art of Hangman
- Displays the word progress after each guess
- Shows used letters to prevent duplicate guesses
- Victory and defeat messages

## Improvement
- User can enter only one letter. Not more than one letter or any number or symbols.

## Requirements
- Python 3.x

## Installation
1. Clone this repository or download the script.
   ```bash
   git clone https://github.com/SoumyadeepRaySamanta/Hangman-Game
   ```
2. Navigate to the project directory.
   ```bash
   cd hangman-game
   ```
3. Run the script.
   ```bash
   python hangman.py
   ```

## How to Play
1. The game will randomly choose a word.
2. You have to guess the word by entering one letter at a time.
3. If the letter is in the word, it will be revealed in the correct position.
4. If the letter is not in the word, you lose an attempt.
5. The game ends when you either guess the word correctly or run out of attempts.

## Example Gameplay
```
  _                                            
 | |                                           
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/    

_________
Guess a letter: d
_________
You guessed d, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
      |
      |
      |
=========
*******************************************5/6 LIVES LEFT*******************************************
```

## Contributions
Feel free to contribute by improving the game logic, adding a GUI, or enhancing the word list. Fork the repository, make changes, and submit a pull request.

## License
This project is open-source and available under the MIT License.

## Author
Soumyadeep Ray Samanta

