import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
length = 100
angle = -60
def exercise_4():
    for i in range(6):
        t.forward(length)
        t.setheading(angle*(i+1))
    t.setheading(angle)
    t.forward(2*length)
    t.setheading(-3*angle)
    t.up()
    t.forward(length)
    t.setheading(-1*angle)
    t.down()
    t.forward(2*length)
    t.up()
    t.setheading(angle)
    t.forward(length)
    t.setheading(3 * angle)
    t.down()
    t.forward(2 * length)
    screen.exitonclick()
exercise_4()