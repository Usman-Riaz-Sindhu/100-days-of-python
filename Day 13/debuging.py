# to solve the bug we have to know about the bug or what thing is creating the bug 
# for example if we have a function that is not working properly we can use print statements to see what is happening inside the function
import random
list1 = [1, 2, 3, 4, 5]
num = random.randint(1, 6)
print(list1[num])
# in this example the bug will only create when random number is 6 we can solve this peoblem by creating our own bug like printing the only one index at a time 

# always fix the bug before you move forward


try:
    age = int(input("Enter your age: "))
except ValueError:
    print("type in numerical form like 17")
    age = int(input("Enter your age: "))
if age >= 18:
    print(f"You age is {age} and you can have an I'd card now!")
else:
    print("you are under age for having an I'd card")
    
# this is called try catch block where we can print any thing instead of an error showing and stoping our program.