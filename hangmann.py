"""
Hangman Game
A simple text-based Hangman game where the player guesses a word one letter at a time.

Key concepts used: random, while loop, if-else, strings, lists.
"""

import random

# Predefined list of words to choose from
WORD_LIST = ["python", "hangman", "keyboard", "science", "developer"]

MAX_INCORRECT_GUESSES = 6


def choose_word(word_list):
    """Randomly select a word from the word list."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Show the word with unguessed letters replaced by underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORD_LIST)
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("Word: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("\nGuess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            # Check if the player has won
            if all(letter in guessed_letters for letter in word):
                print("Word: " + display_word(word, guessed_letters))
                print(f"\nCongratulations! You guessed the word: '{word}'!")
                return
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    # If the loop ends without returning, the player has lost
    print("Word: " + display_word(word, guessed_letters))
    print(f"\nGame over! You've used all {MAX_INCORRECT_GUESSES} incorrect guesses.")
    print(f"The word was: '{word}'")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("\nThanks for playing Hangman!")


if __name__ == "__main__":
    main()