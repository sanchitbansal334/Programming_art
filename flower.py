import turtle

turtle.bgcolor("black")
def curve(x) :
    for i in range(90):
        x.right(1)
        x.forward(1)

#flower
a=turtle.Turtle()
a.color("red")
a.speed(0)
a.pensize(2)
a.begin_fill()
a.left(180)
curve(a)
a.forward(100)
a.right(135)
a.forward(50)
a.left(90)
a.forward(50)
a.right(90)
a.forward(50)
a.left(90)
a.forward(50)
a.right(135)
a.forward(100)
curve(a)
a.forward(25)
a.end_fill()
a.hideturtle()

#stem
b = turtle.Turtle()
b.color("green")
b.pensize(2)
b.begin_fill()
b.forward(15)
b.right(90)
b.forward(300)
b.right(90)
b.forward(15)
b.right(90)
b.forward(300)
b.end_fill()
b.hideturtle()

#leaf
c = turtle.Turtle()
c.color("green")
c.pensize(2)
c.begin_fill()
c.forward(15)
c.right(90)
c.forward(120)
c.left(120)
c.forward(30)
c.left(45)
for i in range(90):
    c.forward(1)
    c.right(1)
c.right(90)
for i in range(90):
    c.forward(1)
    c.right(1)
c.left(45)
c.forward(30)
c.end_fill()
c.hideturtle()


turtle.exitonclick()
