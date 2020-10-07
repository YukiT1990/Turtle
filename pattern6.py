import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
def draw(length=100, digree=144):
  t.forward(length)
  t.right(digree)
for _ in range(5):
  draw()
screen.exitonclick()