import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)

    # Blackjack
    if score == 21 and len(hand) == 2:
        return 0

    # Ace handling
    while 11 in hand and score > 21:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score


def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw!"

    if dealer_score == 0:
        return "Dealer has Blackjack. You lose!"

    if player_score == 0:
        return "Blackjack! You win!"

    if player_score > 21:
        return "You went over 21. You lose!"

    if dealer_score > 21:
        return "Dealer went over 21. You win!"

    if player_score > dealer_score:
        return "You win!"

    return "Dealer wins!"


def play_game():
    print("\n" * 20)
    print(art.logo)

    player = []
    dealer = []

    for _ in range(2):
        player.append(deal_card())
        dealer.append(deal_card())

    game_over = False

    while not game_over:

        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)

        print(f"\nYour cards: {player}, current score: {player_score}")
        print(f"Dealer's first card: {dealer[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, 'n' to pass: ").lower()

            if choice == "y":
                player.append(deal_card())
            else:
                game_over = True

    while calculate_score(dealer) != 0 and calculate_score(dealer) < 17:
        dealer.append(deal_card())

    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    print("\n========== FINAL RESULT ==========")
    print(f"Your cards: {player}, final score: {player_score}")
    print(f"Dealer's cards: {dealer}, final score: {dealer_score}")

    print(compare(player_score, dealer_score))


while True:
    start = input("\nDo you want to play Blackjack? (y/n): ").lower()

    if start == "y":
        play_game()
    elif start == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter y or n.")