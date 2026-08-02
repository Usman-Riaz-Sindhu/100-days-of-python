import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']    
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to random password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for letter in range(nr_letters):
    password.append(random.choice(letters))
for symbol in range(nr_symbols):
    password.append(random.choice(symbols))
for number in range(nr_numbers):
    password.append(random.choice(numbers))

print("Your generated password is:", ''.join(password))


# another way to do this is to shuffle the password list and then join it to make a string
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


print("Welcome to Random Password Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

for i in range(nr_letters):
    password.append(random.choice(letters))

for i in range(nr_symbols):
    password.append(random.choice(symbols))

for i in range(nr_numbers):
    password.append(random.choice(numbers))

# Characters ko random order mein mix karna
random.shuffle(password)

# List ko string mein convert karna
final_password = "".join(password)

print("Your generated password is:", final_password)