import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
def draw_square(length: int):
    for i in range(4):
        t.forward(length)
        t.right(90)
def exercise_3():
    draw_square(200)
    t.up()
    t.goto(-100, -100)
    t.down()
    draw_square(200)
    screen.exitonclick()
exercise_3()