import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Select a difficulty level:")
print("1. Easy (10 attempts)")
print("2. Medium (7 attempts)")
print("3. Hard (5 attempts)")

user_choice = input("Enter your choice (1, 2, or 3): ")
number_to_guess = random.randint(1, 100)

if user_choice == "1":
    total_attempts = 10
    print(f"You have {total_attempts} attempts to guess the number.")
    while total_attempts > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess < number_to_guess:
            print("Too low.")
        elif user_guess > number_to_guess:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number_to_guess}.")
            break
        total_attempts -= 1
        if total_attempts == 0:
            print(f"You've run out of attempts. The number was {number_to_guess}.")
            
elif user_choice == "2":
    total_attempts = 7
    print(f"You have {total_attempts} attempts to guess the number.")
    while total_attempts > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess < number_to_guess:
            print("Too low.")
        elif user_guess > number_to_guess:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number_to_guess}.")
            break
        total_attempts -= 1
        if total_attempts == 0:
            print(f"You've run out of attempts. The number was {number_to_guess}.")

elif user_choice == "3":
    total_attempts = 5
    print(f"You have {total_attempts} attempts to guess the number.")
    while total_attempts > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess < number_to_guess:
            print("Too low.")
        elif user_guess > number_to_guess:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number_to_guess}.")
            break
        total_attempts -= 1
        if total_attempts == 0:
            print(f"You've run out of attempts. The number was {number_to_guess}.")

else:
    print("Invalid choice. Please restart the game and select a valid difficulty level.")