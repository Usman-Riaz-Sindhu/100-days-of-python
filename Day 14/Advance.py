import random

cars = {
    "Toyota Supra": {
        "horsepower": 382,
        "top_speed": 155,
        "price": 56000
    },
    "Nissan GTR": {
        "horsepower": 565,
        "top_speed": 196,
        "price": 121000
    },
    "BMW M3": {
        "horsepower": 503,
        "top_speed": 180,
        "price": 78000
    },
    "Audi R8": {
        "horsepower": 602,
        "top_speed": 205,
        "price": 160000
    },
    "Ford Mustang GT": {
        "horsepower": 480,
        "top_speed": 155,
        "price": 43000
    },
    "Porsche 911": {
        "horsepower": 443,
        "top_speed": 191,
        "price": 120000
    },
    "Mercedes AMG GT": {
        "horsepower": 577,
        "top_speed": 198,
        "price": 140000
    },
    "Chevrolet Corvette": {
        "horsepower": 495,
        "top_speed": 194,
        "price": 67000
    }
}


categories = ["horsepower", "top_speed", "price"]

score = 0
streak = 0
best_streak = 0
round_number = 0

used_pairs = set()

print("""
========================================
          🏎 HIGHER OR LOWER 🏎
========================================
Compare the two cars and guess which
one has the higher value.
========================================
""")


while True:

    # Select two cars
    available_cars = list(cars.keys())

    while True:
        car_a, car_b = random.sample(available_cars, 2)

        pair = tuple(sorted([car_a, car_b]))

        if pair not in used_pairs:
            used_pairs.add(pair)
            break

    # Select random category
    category = random.choice(categories)

    value_a = cars[car_a][category]
    value_b = cars[car_b][category]

    round_number += 1

    print(f"\n---------- ROUND {round_number} ----------")
    print(f"A: {car_a}")
    print(f"B: {car_b}")

    # Make category look nicer
    category_name = category.replace("_", " ").title()

    print(f"\nWhich car has higher {category_name}?")
    print("A -", car_a)
    print("B -", car_b)

    while True:
        answer = input("\nYour answer (A/B): ").strip().upper()

        if answer in ["A", "B"]:
            break

        print("Invalid input! Please enter A or B.")

    # Determine correct answer
    if value_a > value_b:
        correct_answer = "A"
    elif value_b > value_a:
        correct_answer = "B"
    else:
        correct_answer = "TIE"

    # Check result
    if correct_answer == "TIE":

        print("\n🤝 It's a tie!")

        score += 1
        streak += 1

    elif answer == correct_answer:

        score += 1
        streak += 1

        if streak > best_streak:
            best_streak = streak

        print("\n✅ CORRECT!")

        if streak >= 3:
            print(f"🔥 {streak} answer streak!")

    else:

        print("\n❌ WRONG!")

        print(f"{car_a}: {value_a}")
        print(f"{car_b}: {value_b}")

        print("\n================================")
        print("           GAME OVER")
        print("================================")

        print(f"Rounds played: {round_number}")
        print(f"Final score: {score}")
        print(f"Best streak: {best_streak}")

        break

    print(f"Score: {score}")
    print(f"Current streak: {streak}")