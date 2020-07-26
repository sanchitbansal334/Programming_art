import turtle

colors = ["red", "yellow" , "green" , "purple" , "blue" , "orange"]

t = turtle.Pen()
turtle.bgcolor("black")
t.speed(10)
for x in range (200):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.exitonclick()
