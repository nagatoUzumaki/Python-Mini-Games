import turtle
#Game Screen Configuration

window = turtle.Screen()
window.title("Pong Game")
window.setup(1366, 768)
window.bgcolor("black")
window.tracer(0)

#Box
right = turtle.Turtle()
right.shape("square")
right.color("white")
right.shapesize(stretch_wid = 30, stretch_len = 0.1)
right.penup()
right.goto(+620, 0)

left = turtle.Turtle()
left.shape("square")
left.color("white")
left.shapesize(stretch_wid = 30, stretch_len = 0.1)
left.penup()
left.goto(-620, 0)

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
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid = 6, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-600, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid = 6, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(600, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("magenta")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 1.5
