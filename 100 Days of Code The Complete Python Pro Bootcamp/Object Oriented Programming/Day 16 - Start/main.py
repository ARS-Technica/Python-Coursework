"""
Turtle Graphics Documentation
https://docs.python.org/3/library/turtle.html

Turtle Colours
https://cs111.wellesley.edu/reference/colors
"""

import another_module
print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkRed")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
