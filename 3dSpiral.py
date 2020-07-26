import turtle
from random import randint
win = turtle.Screen()
win.bgcolor("black")
t=turtle.Turtle()
x=1
t.speed(0)
t.shape("turtle")

while x<400:
	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)
	turtle.colormode(255)
	t.color(r,g,b)
	t.forward(5+x)
	t.right(91)
	x=x+1
t.hideturtle()
turtle.exitonclick()