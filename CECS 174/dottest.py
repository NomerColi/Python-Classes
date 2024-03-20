from random import randint, choice
from turtle import Turtle, Screen

COLORS = ['red', 'green', 'blue', 'magenta', 'yellow', 'cyan']

screen = Screen()

width, height = screen.window_width(), screen.window_height()

turtle = Turtle(visible=False)
turtle.speed('fastest')
turtle.penup()

for _ in range(randint(10, 100)):
    radius = randint(5, 45)

    x = randint(radius - width//2, width//2 - radius)
    y = randint(radius - height//2, height//2 - radius)

    print("Dot pos x :", x, "y :", y)

    turtle.setposition(x, y)
    turtle.dot(radius * 2, choice(COLORS))

screen.exitonclick()
