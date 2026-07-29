from turtle import Turtle ,Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600,600)
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()
    #detect collision with food
    if snake.segments[0].distance(food)<15:
        print("eaten")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    
    # Detect collision with wall
    if (snake.segments[0].xcor() > 280 or
        snake.segments[0].xcor() < -280 or
        snake.segments[0].ycor() > 280 or
        snake.segments[0].ycor() < -280):

        print("GAME OVER")
        scoreboard.game_over()
        game_is_on = False

    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            



screen.exitonclick()