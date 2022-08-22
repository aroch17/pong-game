import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Stop animation
screen.tracer(0)

# Making a paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Score()

# Moving the paddle
screen.listen()

screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    # slowing down animation
    time.sleep(ball.move_speed)
    # Continuously updating screen
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 40 and ball.xcor() > 330:
        ball.bounce_off_paddle()
    if ball.distance(l_paddle) < 40 and ball.xcor() > -330:
        ball.bounce_off_paddle()

    # Detect wall out of bounds
    if ball.xcor() > 400:
        score.l_point()
        ball.reset_pos()

    if ball.xcor() < -400:
        score.r_point()
        ball.reset_pos()

screen.exitonclick()
