# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#         print(i)
    
# my_function()

for number in range(1, 21):
    is_prime = True

    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print("Prime number found!")
    else:
        print(number)
        
        
        
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# game solution

# def turn_right():
#     for i in range(5):
#         turn_left()
    
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()