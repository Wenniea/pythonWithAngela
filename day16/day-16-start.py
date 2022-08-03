import turtle

# from turtle import Turtle, Screen
# timmy = Turtle()  #created an object timmy from the turtle class
# timmy.shape('turtle')
# timmy.color('purple')
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

