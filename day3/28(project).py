# treasue island game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("Enter your choice (left or right): ").strip().lower()
if choice1 == "left":
    choice2 = input("swim or wait: ").strip().lower()
    if choice2 == "wait":
        choice3 = input("Which door? (red, blue, yellow): ").strip().lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry crocodile. Game Over.")    
else:
    print("You fell into a hole. Game Over.")