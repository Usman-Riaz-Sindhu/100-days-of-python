# enimies = 1 #global scope
# def increase_enemies():
    # enimies = 2 #local scope
    # print(f"Inside function {enimies}.")
    
# increase_enemies()
# print(f"Outside function {enimies}.")

# if we wanna use the global variable inside a function or loop we can use the global keyword
# do not modify the global variable inside a function or loop without using the global keyword, it will create a new local variable with the same name instead of modifying the global variable.



enemy = 1 #global scope
def increase_enemies(enemy):
    print(f"Inside function {enemy}.") 
    return enemy + 1 #local scope
    
enemies = increase_enemies(enemy)
print(f"Outside function {enemies}.")
