from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
user_level = screen.textinput("Make your level", prompt="Which level do you "
                              "want to play this game at? Enter a level "
                              "(easy, normal, hard): ")
speed_level = [0.2, 0.1, 0.05]
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

if user_level:
    game_is_on = True

while game_is_on:
    screen.update()
    if user_level == "easy":
        time.sleep(speed_level[0])
    elif user_level == "normal":
        time.sleep(speed_level[1])
    elif user_level == "hard":
        time.sleep(speed_level[2])
    else:
        user_level = screen.textinput("Make your level", prompt="Which level do you "
                              "want to play this game at? Enter a level "
                              "(easy, normal, hard): ")
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()