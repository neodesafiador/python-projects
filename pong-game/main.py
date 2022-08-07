from time import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ALIGN = "center"
FONT = ("Courier", 24, "normal")
SCORE_TO_WIN = 3

# Set the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)    # in order to turn off the animation

# Create a right paddle anf left one
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create a ball
ball = Ball()

# Create a scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

    # Stop the game when left player wins
    if scoreboard.l_score == SCORE_TO_WIN:
        scoreboard.goto(0, 50)
        scoreboard.write("The LEFT side player wins !!", align=ALIGN, font=FONT)
        game_on = False

    # Stop the game when right player wins
    if scoreboard.r_score == SCORE_TO_WIN:
        scoreboard.goto(0, 50)
        scoreboard.write("The RIGHT side player wins !!", align=ALIGN, font=FONT)
        game_on = False


screen.exitonclick()
