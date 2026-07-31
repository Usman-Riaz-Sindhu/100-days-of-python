import random

# my_num = random.randint(1, 10)
# print("my_num is:", my_num)

# number2 = random.random()  # generates a random float between 0 and 1
# print("number2 is:", number2)

# number3 = random.uniform(1, 10)  # generates a random float between 1 and 10
# print("number3 is:", number3)

toss = random.randint(0, 1)  # generates a random integer between 0 and 1
if toss == 0:
    print("toss is: Heads")
else:
    print("toss is: Tails")