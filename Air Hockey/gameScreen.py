import turtle
#Game Screen Configuration

window = turtle.Screen()
window.title("Pong Game")
window.setup(1366, 768)
window.bgcolor("black")
window.tracer(0)

#Box
rightl = turtle.Turtle()
rightl.shape("square")
rightl.color("white")
rightl.shapesize(stretch_wid = 10, stretch_len = 0.1)
rightl.penup()
rightl.goto(+620, -200)

leftl = turtle.Turtle()
leftl.shape("square")
leftl.color("white")
leftl.penup()
leftl.shapesize(stretch_wid = 10, stretch_len = 0.1)
leftl.goto(-620, -200)


rightu = turtle.Turtle()
rightu.shape("square")
rightu.color("white")
rightu.shapesize(stretch_wid = 10, stretch_len = 0.1)
rightu.penup()
rightu.goto(+620, 200)

leftu = turtle.Turtle()
leftu.shape("square")
leftu.color("white")
leftu.penup()
leftu.shapesize(stretch_wid = 10, stretch_len = 0.1)
leftu.goto(-620, 200)

circle = turtle.Turtle()
#circle.shape("circle")
circle.color("white")
#circle.circle(10)
circle.penup()
circle.setposition(0, -100)
circle.pendown()
circle.circle(100)

center = turtle.Turtle()
center.shape("square")
center.color("white")
center.shapesize(stretch_wid = 30, stretch_len = 0.1)
center.penup()
center.goto(0, 0)

top = turtle.Turtle()
top.shape("square")
top.color("white")
top.shapesize(stretch_wid = 0.1, stretch_len = 62)
top.penup()
top.goto(0, 300)

bottom = turtle.Turtle()
bottom.shape("square")
bottom.color("white")
bottom.shapesize(stretch_wid = 0.1, stretch_len = 62)
bottom.penup()
bottom.goto(0, -300)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid = 3, stretch_len = 3)
paddle_a.penup()
paddle_a.goto(-600, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("circle")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid = 3, stretch_len = 3)
paddle_b.penup()
paddle_b.goto(600, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("magenta")
ball.shapesize(stretch_wid = 2, stretch_len = 2)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 1.4
