height = int(input("Enter your height in cm: "))
bill = 0
if height >= 150:
    print("You are tall enough to ride the roller coaster.")
    age = int(input("Enter your age: "))
    if age >= 18:
        bill = 20
        print(f"Your ticket is ${bill}.")
    elif age >= 12:
        bill = 10
        print(f"Your ticket is ${bill}.")
        
    want_photo = input("Do you want a photo taken? (yes/no): ").strip().lower()
    if want_photo == "yes":
        bill += 3
        print(f"Your final bill is ${bill}.")
    else:
        print("You are not tall enough to ride the roller coaster.")