import turtle

turtle.bgcolor("black")
def curve(x) :
    for i in range(200):
        x.right(1)
        x.forward(1)

a = turtle.Turtle()
a.pensize(3)
a.speed(20)
a.color("red" , "pink")
a.begin_fill()
a.left(140)
a.forward(111.65)
curve(a)

a.left(120)
curve(a)
a.forward(111.65)
a.end_fill()
a.hideturtle()
turtle.exitonclick()
