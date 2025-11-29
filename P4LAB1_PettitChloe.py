import turtle

tim = turtle.Turtle()
turtle.bgcolor("lightyellow")
tim.fillcolor("darkgreen")

tim.begin_fill()
for side in range(4):
    tim.forward(100)
    tim.right(90)
tim.end_fill()

tim.fillcolor("lightgreen")

tim.begin_fill()
for side in range(3):
    tim.forward(100)
    tim.left(120)
tim.end_fill()

turtle.done()
