# # import turtle
# from turtle import Turtle, Screen
# # this works same as above but the only difference is now we dont need to call by turtle.Turtle we can simply do timy = Turtle()

# timy = Turtle()
# print(timy)
# timy.shape("turtle")
# timy.color("DarkGreen") 
# timy.speed(2)
# timy.forward(200)   # aagay 100 pixels
# timy.backward(50)   # peechay 50 pixels

# timy.right(90)      # right 90° turn
# timy.left(90)       # left 90° turn


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Names", ["Usman", "Ali", "Zain", "Abdullah"])
table.add_column("Marks", [20, 20, 18, 19])
print(table)
