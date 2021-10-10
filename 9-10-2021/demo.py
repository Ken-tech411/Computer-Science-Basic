import turtle

wn = turtle.Screen()

pen = turtle.Turtle()

pen.speed(1)
pen.pendown()
pen.color("black", "aliceblue")
pen.begin_fill()
pen.forward(100)
pen.left(120)
pen.forward(100)

pen.forward(100)
pen.left(120)
pen.forward(100)

pen.forward(100)
pen.left(120)
pen.forward(100)

pen.end_fill()

pen.penup()
turtle.done()

