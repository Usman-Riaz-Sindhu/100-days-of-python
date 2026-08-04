import art

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        if letter in alphabets:
            new_position = (alphabets.index(letter) + shift_amount) % 26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += letter

    print(f"The encoded text is {cipher_text}")


def decrypt(original_text, shift_amount):
    decipher_text = ""

    for letter in original_text:
        if letter in alphabets:
            new_position = (alphabets.index(letter) - shift_amount) % 26
            decipher_text += alphabets[new_position]
        else:
            decipher_text += letter

    print(f"The decoded text is {decipher_text}")


# Program repeat karne ke liye
again = "yes"

while again == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)

    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)

    else:
        print("Invalid input. Please type 'encode' or 'decode'.")

    again = input("Do you want to run the program again? Type 'yes' or 'no':\n").lower()

print("Goodbye!")