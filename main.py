from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.tracer(0)


wall_mode = screen.textinput(
    "Choose Wall Mode",
    "Type 1 for Classic (wall = game over)\nType 2 for Wraparound (Snake II style)\n\nEnter 1 or 2:"
)


while wall_mode not in ("1", "2"):
    wall_mode = screen.textinput(
        "Invalid Input",
        "Please type 1 or 2 only.\n\nEnter 1 or 2:"
    )

wraparound_enabled = (wall_mode == "2")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        print("eaten")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if wraparound_enabled:
        # Snake II style - teleport to the opposite edge instead of dying
        if (snake.segments[0].xcor() > 280) or (snake.segments[0].xcor() < -280):
            snake.segments[0].goto(x=-snake.segments[0].xcor(), y=snake.segments[0].ycor())

        if (snake.segments[0].ycor() > 280) or (snake.segments[0].ycor() < -280):
            snake.segments[0].goto(x=snake.segments[0].xcor(), y=-snake.segments[0].ycor())

    else:
        # Classic style - hitting any wall ends the game
        if (snake.segments[0].xcor() > 280 or
            snake.segments[0].xcor() < -280 or
            snake.segments[0].ycor() > 280 or
            snake.segments[0].ycor() < -280):

            print("GAME OVER")
            scoreboard.game_over()
            game_is_on = False

    # Detect collision with tail (applies in both modes)
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
