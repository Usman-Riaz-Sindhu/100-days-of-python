import random

# Global variable
number_to_guess = random.randint(1, 100)


def play_game(total_attempts):
    # total_attempts is a local variable/parameter
    print(f"You have {total_attempts} attempts to guess the number.")

    while total_attempts > 0:
        # user_guess is a local variable
        user_guess = int(input("Make a guess: "))

        if user_guess < number_to_guess:
            print("Too low.")

        elif user_guess > number_to_guess:
            print("Too high.")

        else:
            print(f"You got it! The answer was {number_to_guess}.")
            return

        total_attempts -= 1

        print(f"You have {total_attempts} attempts left.")

    print(f"You've run out of attempts. The number was {number_to_guess}.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Select a difficulty level:")
print("1. Easy (10 attempts)")
print("2. Medium (7 attempts)")
print("3. Hard (5 attempts)")

user_choice = input("Enter your choice (1, 2, or 3): ")

if user_choice == "1":
    play_game(10)

elif user_choice == "2":
    play_game(7)

elif user_choice == "3":
    play_game(5)

else:
    print("Invalid choice. Please restart the game.")