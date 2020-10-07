import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
def draw_square(length: int):
    for i in range(4):
        t.forward(length)
        t.right(90)
def exercise_1():
    draw_square(250)
    t.up()
    t.goto(-50, 50)
    t.down()
    draw_square(350)
    screen.exitonclick()
exercise_1()