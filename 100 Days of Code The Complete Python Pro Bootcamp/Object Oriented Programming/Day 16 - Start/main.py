"""
Turtle Graphics Documentation
https://docs.python.org/3/library/turtle.html

Turtle Colours
https://cs111.wellesley.edu/reference/colors

PrettyTable
https://pypi.org/project/prettytable/

PrettyTable Tutorial
https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
"""

# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkRed")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmader"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# print(table.align)

table.align = "l"   # Left align
print(table)

