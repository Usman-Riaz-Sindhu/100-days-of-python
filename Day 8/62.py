def greet_name(name, age, city):
    print(f"Nice to meet you, {name}!")
    print(f"Great to see you! You are turning {age} years old!")
    print(f"Welcome to {city}!")
greet_name("Usman", 25, "New York")

# if we change the position of argument and pass the values in a different order, it will lead to incorrect output
# in pyhton this is calles positional arguments. The order of the arguments matters and must match the order of the parameters in the function definition.

def greet_name(name, age, city):
    print(f"Nice to meet you, {name}!")
    print(f"Great to see you! You are turning {age} years old!")
    print(f"Welcome to {city}!")
greet_name(age = 25, name = "Usman", city = "New York")
# this is called keyword arguments. The order of the arguments does not matter when using keyword arguments, as long as the correct parameter names are used.