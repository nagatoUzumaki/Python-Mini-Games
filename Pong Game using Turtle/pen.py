import turtle

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.penup()
pen.hideturtle()

def pen_update(score_a, score_b):
    pen.clear()
    pen.goto(-600, 300)
    pen.color("Blue")
    pen.write("Player Blue: {}".format(score_a), align="left", font=("Courier", 24, "normal"))
    pen.color("red")
    pen.goto(600, 300)
    pen.write("Player Red: {}".format(score_b), align="right", font=("Courier", 24, "normal"))
