import turtle
win = turtle.Screen()
win.title("Animation")
t = turtle.Turtle()
t.color("green")
t.hideturtle()
t.speed(0)
for i in range(100):
	t.circle(i*2)
	t._rotate(5)

turtle.exitonclick()