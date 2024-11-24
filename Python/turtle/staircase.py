import turtle

t = turtle.Turtle()
step_size = 25

for i in range(1):
    t.penup()

    t.goto(-step_size * i, 1.5 * step_size * i)

    t.pendown()

    for _ in range(10):
        t.left(90)
        t.forward(step_size)
        t.right(90)
        t.forward(step_size)

turtle.exitonclick()