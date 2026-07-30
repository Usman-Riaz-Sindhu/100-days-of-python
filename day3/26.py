# pizza order practice 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").strip().upper()
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25


pepperoni = input("Do you want pepperoni? Y or N: ").strip().upper()
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 5
    else:
        bill += 8


extra_cheese = input("Do you want extra cheese? Y or N: ").strip().upper()
if extra_cheese == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 4
    else:
        bill += 6

print(f"Your final bill is ${bill}.")