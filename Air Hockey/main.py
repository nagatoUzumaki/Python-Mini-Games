import turtle
import os
import pen
import gameScreen

#gameScreen.screen()
#Scores
score_a = 0
score_b = 0
#pen.pen_update(score_a, score_b)


#Paddle Movement Functions
def paddle_a_up():
    if gameScreen.paddle_a.ycor() < 240:
        y = gameScreen.paddle_a.ycor()
        y += 30
        gameScreen.paddle_a.sety(y)

def paddle_a_down():
    if gameScreen.paddle_a.ycor() > -240:
        y = gameScreen.paddle_a.ycor()
        y -= 30
        gameScreen.paddle_a.sety(y)

def paddle_b_up():
    if gameScreen.paddle_b.ycor() < 240:
        y = gameScreen.paddle_b.ycor()
        y += 30
        gameScreen.paddle_b.sety(y)

def paddle_b_down():
    if gameScreen.paddle_b.ycor() > -240:
        y = gameScreen.paddle_b.ycor()
        y -= 30
        gameScreen.paddle_b.sety(y)

# Keyboard bindings
gameScreen.window.listen()
gameScreen.window.onkeypress(paddle_a_up, "w")
gameScreen.window.onkeypress(paddle_a_down, "s")
gameScreen.window.onkeypress(paddle_b_up, "Up")
gameScreen.window.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    gameScreen.window.update()

    #ball Movement
    gameScreen.ball.setx(gameScreen.ball.xcor() + gameScreen.ball.dx)
    gameScreen.ball.sety(gameScreen.ball.ycor() + gameScreen.ball.dy)

    #ball bounce
    if gameScreen.ball.ycor() > 300:
        gameScreen.ball.dy *= -1
        gameScreen.ball.sety(300)

    if gameScreen.ball.ycor() < -300:
        gameScreen.ball.dy *= -1
        gameScreen.ball.sety(-300)

    if gameScreen.ball.xcor() > 600:
        gameScreen.ball.goto(0, 0)
        gameScreen.ball.dx *= -1
        score_a += 1
        pen.pen_update(score_a, score_b)

    if gameScreen.ball.xcor() < -600:
        gameScreen.ball.goto(0, 0)
        gameScreen.ball.dx *= -1
        score_b += 1
        pen.pen_update(score_a, score_b)

    if gameScreen.ball.xcor() > 590 and gameScreen.ball.ycor() < gameScreen.paddle_b.ycor() + 60 and gameScreen.ball.ycor() > gameScreen.paddle_b.ycor() - 60:
        gameScreen.ball.dx *= -1

    if gameScreen.ball.xcor() < -590 and gameScreen.ball.ycor() < gameScreen.paddle_a.ycor() + 60 and gameScreen.ball.ycor() > gameScreen.paddle_a.ycor() - 60:
        gameScreen.ball.dx *= -1
