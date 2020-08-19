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
    if gameScreen.paddle_a.ycor() < 270:
        y = gameScreen.paddle_a.ycor()
        y += 30
        gameScreen.paddle_a.sety(y)

def paddle_a_down():
    if gameScreen.paddle_a.ycor() > -270:
        y = gameScreen.paddle_a.ycor()
        y -= 30
        gameScreen.paddle_a.sety(y)

def paddle_b_up():
    if gameScreen.paddle_b.ycor() < 270:
        y = gameScreen.paddle_b.ycor()
        y += 30
        gameScreen.paddle_b.sety(y)

def paddle_b_down():
    if gameScreen.paddle_b.ycor() > -270:
        y = gameScreen.paddle_b.ycor()
        y -= 30
        gameScreen.paddle_b.sety(y)

def paddle_a_left():
    if gameScreen.paddle_a.xcor() > -500:
        x = gameScreen.paddle_a.xcor()
        x -= 30
        gameScreen.paddle_a.setx(x)

def paddle_a_right():
    if gameScreen.paddle_a.xcor() < -100:
        x = gameScreen.paddle_a.xcor()
        x += 30
        gameScreen.paddle_a.setx(x)

def paddle_b_left():
    if gameScreen.paddle_b.xcor() > 100:
        x = gameScreen.paddle_b.xcor()
        x -= 30
        gameScreen.paddle_b.setx(x)

def paddle_b_right():
    if gameScreen.paddle_b.xcor() < 500:
        x = gameScreen.paddle_b.xcor()
        x += 30
        gameScreen.paddle_b.setx(x)


# Keyboard bindings
gameScreen.window.listen()
gameScreen.window.onkeypress(paddle_a_up, "w")
gameScreen.window.onkeypress(paddle_a_down, "s")
gameScreen.window.onkeypress(paddle_b_up, "Up")
gameScreen.window.onkeypress(paddle_b_down, "Down")
gameScreen.window.onkeypress(paddle_a_left, "a")
gameScreen.window.onkeypress(paddle_a_right, "d")
gameScreen.window.onkeypress(paddle_b_left, "Left")
gameScreen.window.onkeypress(paddle_b_right, "Right")

#Main game loop
while True:
    gameScreen.window.update()

    #ball Movement
    gameScreen.ball.setx(gameScreen.ball.xcor() + gameScreen.ball.dx)
    gameScreen.ball.sety(gameScreen.ball.ycor() + gameScreen.ball.dy)

    #ball bounce
    if gameScreen.ball.ycor() > 300:
        gameScreen.ball.dy *= -0.8
        gameScreen.ball.sety(300)

    if gameScreen.ball.ycor() < -300:
        gameScreen.ball.dy *= -0.8
        gameScreen.ball.sety(-300)

    if gameScreen.ball.xcor() > 620 and abs(gameScreen.ball.ycor()) > 100:
        gameScreen.ball.dx *= -0.8
        gameScreen.ball.setx(620)

    if gameScreen.ball.xcor() < -620 and abs(gameScreen.ball.ycor()) > 100:
        gameScreen.ball.dx *= -0.8
        gameScreen.ball.setx(-620)

    if gameScreen.ball.xcor() > 600 and gameScreen.ball.ycor() < 60 and gameScreen.ball.ycor() > -60:
        gameScreen.ball.goto(0, 0)
        gameScreen.ball.dx *= -1
        score_a += 1
        pen.pen_update(score_a, score_b)

    if gameScreen.ball.xcor() < -600  and gameScreen.ball.ycor() < 60 and gameScreen.ball.ycor() > -60:
        gameScreen.ball.goto(0, 0)
        gameScreen.ball.dx *= -1
        score_b += 1
        pen.pen_update(score_a, score_b)

    if abs(gameScreen.ball.ycor() - gameScreen.paddle_b.ycor()) < 30 and abs(gameScreen.ball.xcor() - gameScreen.paddle_b.xcor()) < 30:
        gameScreen.ball.dx *= -1.2
        gameScreen.ball.dy *= -1.3

    if abs(gameScreen.ball.ycor() - gameScreen.paddle_a.ycor()) < 30 and abs(gameScreen.ball.xcor() - gameScreen.paddle_a.xcor()) < 30:
        gameScreen.ball.dx *= -1.2
        gameScreen.ball.dy *= -1.3
