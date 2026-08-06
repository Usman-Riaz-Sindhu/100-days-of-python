num1 = int(input("Enter the first number: "))
task = input("Enter the task you want to perform (+, -, *, /): ")
num2 = int(input("Enter the second number: "))
retry = True
while retry == True:
    def calculator(num1, num2, task):
        if task == "+":
            return num1 + num2
        elif task == "-":
            return num1 - num2
        elif task == "*":
            return num1 * num2
        elif task == "/":
            return num1 / num2
        else:
            print("Invalid task. Please enter a valid task.")
            
    