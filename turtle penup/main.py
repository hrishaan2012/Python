import turtle
turtle.Screen().bgcolor("lightblue")
t = turtle.Turtle()

for i in range(3):
    t.forward(100)
    t.left(120)


t.penup()
t.left(90)
t.forward(50)
t.right(90)

t.pendown()

for i in range(3):
    t.forward(100)
    t.right(120)
turtle.done()