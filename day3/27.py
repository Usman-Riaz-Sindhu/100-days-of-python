# logical operators 
height = int(input("Enter your height in cm: "))
bill = 0
if height >= 120:
    print("You are tall enough to ride the roller coaster.")
    age = int(input("Enter your age: "))
    if age >= 18:
        bill = 20
        print(f"Your ticket is ${bill}.")
    elif age > 40 and age < 60:
        print("You get a free ride!")
    elif age >= 12:
        bill = 10
        print(f"Your ticket is ${bill}.")
        
    want_photo = input("Do you want a photo taken? (yes/no): ").strip().lower()
    if want_photo == "yes":
        bill += 3
        print(f"Your final bill is ${bill}.")
else:
    print("You are not tall enough to ride the roller coaster.")