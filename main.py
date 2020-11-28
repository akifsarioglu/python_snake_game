from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Example Snake Game with Python")
# If screen.tracer is 0 (off); screen won't refresh after every movement of the objects. we will update the screen
# manually.
screen.tracer(0)

# Creating an instance from Snake class
snake = Snake()

# Creating an instance from Food class
food = Food()

# Creating an instance from Score class to write current score on screen
scoreboard = Score()

# screen.listen method for listen inputs from user
screen.listen()

screen.onkey(snake.turnUp, "Up")
screen.onkey(snake.turnDown, "Down")
screen.onkey(snake.turnLeft, "Left")
screen.onkey(snake.turnRight, "Right")

gameFinished = False

# if game is not finished yet, move the snake forward
while not gameFinished:
    # After every movement process finish and start again, we update the screen
    # and wait for 0.1 seconds to move the squares again.
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Collision between Snake and Food
    if snake.head.distance(food) < 15:
        food.goRandomLocation()
        scoreboard.increaseScore()
        snake.extendSnake()

    # Collision between Snake and the walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameFinished = True
        scoreboard.gameOver()

    # Collision between Snake's head and it's tail
    # We sliced our snake.squares list from 1 to last
    # Because the first square in the list is head itself
    # It will immediately game over if we don't slice the list
    # Because head is always in collision with itself :p
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            gameFinished = True
            scoreboard.gameOver()

screen.exitonclick()
