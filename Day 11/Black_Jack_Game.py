import art
import random
print(art.logo)
print("The goal of the game is to get as close to 21 as possible without going over.")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]

while True:
    start_game = input("Press y to start the game or n to exit the game: ")
    if start_game == "y":
        player_cards = random.choices(cards, k=2)
        print(player_cards)