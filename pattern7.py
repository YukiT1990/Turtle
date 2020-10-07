import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
screen.bgcolor("green")

for i in range(12):
    t.up()
    t.forward(100)
    t.down()
    t.forward(20)
    t.up()
    t.forward(20)
    t.stamp()
    t.goto(0, 0)
    t.left(30)

screen.exitonclick()
