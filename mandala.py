import turtle
#import time
turtle.bgcolor("Black")
turtle.pensize(2)
turtle.speed(20)

for i in range (6):
    for colour in ["red" , "white" , "blue" , "green" , "magenta" , "yellow"]:
        turtle.color(colour)
        turtle.circle(100)
        turtle.left(10)
        #time.sleep(0.5)

turtle.hideturtle()
turtle.exitonclick()
#a = input("Press enter to continue:")
