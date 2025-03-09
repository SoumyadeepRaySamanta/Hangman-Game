# This is Hangman game, Written by Soumyadeep Ray Samanta
import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

# Defining lives, storing corrected inputs and setting the state of the game
lives = 6
placeholder = ""
updated_letters = []
game_over = False

# Choosing the word
chosen_word = random.choice(word_list)

# Placing same number of blanks to be filled
for letter in chosen_word:
    placeholder += "_"
print(placeholder)


while not game_over:
    guess = input("Guess a letter: ").lower() # Taking user input

    # Taking only single letter input, not any other type (i.e., numbers, symbols or mixed)
    while True:
        if len(guess) == 1 and guess.isalpha():     # .isalpha() is a built-in Python string method that checks if all characters in a string are alphabetic (i.e., only letters A-Z or a-z).
            break
        else:
            print("Invalid input! Enter only one letter.")
            guess = input("Guess a letter: ").lower()

    # Checking if user already guessed that letter
    if guess in updated_letters:
        print(f"You've already guessed {guess}")

    # If the guess is correct, replace the letter
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += guess
            updated_letters.append(guess)
        elif letter in updated_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # If the guess is not in the word, deducting the lives by 1
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    # If lives is 0 then Game Over
    print(stages[lives])
    if lives == 0:
        game_over = True
        print(
            f"***********************************IT WAS {chosen_word}! YOU LOSE*******************************************")
    print(f"*******************************************{lives}/6 LIVES LEFT*******************************************")

    # Defining the wining state/condition
    if "_" not in display:
        game_over = True
        print("******************************************YOU WIN**************************************************")

