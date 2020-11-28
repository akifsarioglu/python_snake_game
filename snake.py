from turtle import Turtle

# Default starting positions(x,y) of 3 squares which little parts of our snake.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # We will keep every square of snake in a list to access them quickly later.
        self.squares = []
        self.createSnake()
        self.head = self.squares[0]

    def createSnake(self):
        # Creating first 3 squares with a loop.
        for position in STARTING_POSITIONS:
            self.addSquare(position)

    # This method creates new square by given position
    def addSquare(self, position):
        newSquare = Turtle(shape="square")
        newSquare.color("white")
        newSquare.penup()  # penup() method for remove the trail of squares.
        newSquare.goto(position)
        self.squares.append(newSquare)

    def extendSnake(self):
        self.addSquare(self.squares[-1].position())

    def move(self):
        # this loops replaces the squares each others previous positions.
        # so basically we pushing the snake from it's tail instead of pulling to position from it's head.
        for square_num in range(len(self.squares) - 1, 0, -1):
            newX = self.squares[square_num - 1].xcor()
            newY = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(newX, newY)
        self.squares[0].forward(MOVE_DISTANCE)

    def turnUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turnDown(self):
        if self.head.heading() != UP:
            self.squares[0].setheading(DOWN)

    def turnLeft(self):
        if self.head.heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def turnRight(self):
        if self.head.heading() != LEFT:
            self.squares[0].setheading(RIGHT)
