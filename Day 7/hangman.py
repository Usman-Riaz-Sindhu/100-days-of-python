import random

# List of possible words
words = ["apple", "mango", "house", "tiger", "grape", "peach", "lemon", "berry", "melon"]

# Hangman stages
hangman_art = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======
    """,

    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======
    """,

    """
     +---+
     |   |
         |
         |
         |
         |
    =======
    """
]


def choose_word():
    return random.choice(words)


def create_blanks(word):
    return ["_"] * len(word)


def display_word(blanks):
    print(" ".join(blanks))


def check_guess(word, guess, blanks):
    correct = False

    for index in range(len(word)):
        if word[index] == guess:
            blanks[index] = guess
            correct = True

    return correct


def game():
    word = choose_word()
    blanks = create_blanks(word)

    lives = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the 5 letter word")

    while lives > 0 and "_" in blanks:

        print(hangman_art[lives])
        display_word(blanks)

        print("Guessed letters:", guessed_letters)

        guess = input("Guess a letter: ").lower()

        # Check input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        # Check duplicate guess
        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue

        guessed_letters.append(guess)

        # Check answer
        if check_guess(word, guess, blanks):
            print("Correct guess!")
        else:
            print("Wrong guess!")
            lives -= 1

        print(f"Lives left: {lives}")


    # Game result
    if "_" not in blanks:
        print("\nCongratulations! You won!")
        print("The word was:", word)

    else:
        print(hangman_art[0])
        print("\nGame Over!")
        print("The word was:", word)


# Start game
game()