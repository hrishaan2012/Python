n=int(input("Enter the number of sides of the polygon: "))
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(width=800, height=600)
t=turtle.Turtle()
if n < 3:
    print("A polygon must have at least 3 sides.")
    exit()
num_sides = n
side_length = 100
angle = 360 / num_sides
polgon_color = "blue"

for i in range(num_sides):
    t.color(polgon_color)
    t.forward(side_length)
    t.right(angle)  