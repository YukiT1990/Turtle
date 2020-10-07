import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
def draw_square(length: int):
    t.forward(length / 2)
    t.right(90)
    for i in range(3):
        t.forward(length)
        t.right(90)
    t.forward(length / 2)
def exercise_5():
    for i in range(5):
        draw_square(100)
        t.up()
        t.right(72)
        t.down()
    screen.exitonclick()
t.left(15)
exercise_5()