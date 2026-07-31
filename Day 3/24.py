# # nested if else statements
# age = int(input("Enter your age: "))
# if age >= 12:
#     print("your enterence ticket is $20")
#     if age >= 18:
#         print("you can ride the roller coaster")
#     else:
#         print("you cannot ride the roller coaster")
# else:
#     print("your enterence ticket is $10")

age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ").strip().lower()
if age >= 18:
    if has_license == "yes":
        print("You are eligible to drive.")
    else:
        print("You need a driver's license to drive.")
else:
    print("You are not old enough to drive.")