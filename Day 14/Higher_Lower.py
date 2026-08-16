import random

cars = {
    "Toyota Supra": 382,
    "Nissan GTR": 565,
    "BMW M3": 503,
    "Audi R8": 602,
    "Ford Mustang GT": 480,
    "Porsche 911": 443,
    "Mercedes AMG GT": 577,
    "Chevrolet Corvette": 495
}

score = 0

print("================================")
print("       HIGHER OR LOWER")
print("================================")

while True:

    # Pick two different cars
    car_a, car_b = random.sample(list(cars.keys()), 2)

    print(f"\nA: {car_a}")
    print("VS")
    print(f"B: {car_b}")

    answer = input("Which car has higher horsepower? A or B: ").upper()

    # Determine the correct answer
    if cars[car_a] > cars[car_b]:
        correct_answer = "A"
    else:
        correct_answer = "B"

    # Check answer
    if answer == correct_answer:
        score += 1
        print(f"Correct! 🎉 Your score is {score}")
    else:
        print(f"Wrong! 😢")
        print(f"The correct answer was {correct_answer}")
        print(f"Final score: {score}")
        break