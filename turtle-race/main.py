from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                            "Enter a color (red, orange, yellow, green, blue, purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []    # List to store all turtles

# Create six turtles and set them at the starting point
for turtle_index in range(0, 6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle
        if turtle.xcor() > 230:
            is_race_on = False
            # extract the color of the first turtle to reach the goal
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! The {winning_color} turtle is the winner!!")
            else:
                print(f"You've lost!! The {winning_color} turtle is the winner!!")
        # Make each turtle move a random amount
        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)


screen.exitonclick()