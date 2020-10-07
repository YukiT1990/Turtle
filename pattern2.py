import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
def draw_square(length: int):
    for i in range(4):
        t.forward(length)
        t.right(90)
def exercise_2():
    draw_square(100)
    t.up()
    t.goto(50, 20)
    t.down()
    t.setheading(-45)
    draw_square(100)
    screen.exitonclick()
exercise_2()