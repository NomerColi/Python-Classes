from turtle import Turtle, Screen
import math

screen = Screen()

turtle = Turtle(visible=False)
turtle.speed('fastest')
turtle.penup()

radius = 10
multiplier = 50

i = 0
dotnum = 360

while i < dotnum:
    x = math.cos(math.radians(i)) * multiplier
    y = math.sin(math.radians(i)) * multiplier
    print("Dot pos x :", x, "y :", y)
    turtle.setposition(x, y)
    turtle.dot(radius * 2, 'green')
    i += 10
    
screen.exitonclick()
