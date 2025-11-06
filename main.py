from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Noah's Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# collision with food
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        scoreboard.score_updater()

# collision with wall
    if (snake.head.xcor() > 294 or snake.head.xcor() < - 294
            or snake.head.ycor() > 294 or snake.head.ycor() < - 294):
        game_is_on = False
        scoreboard.game_over_text()

# collision with tail
    for squares in snake.squares[1:]:
        if snake.head.distance(squares) < 10:
            game_is_on = False
            scoreboard.game_over_text()



screen.exitonclick()