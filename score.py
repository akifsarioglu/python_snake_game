from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.writeScore()

    def writeScore(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.writeScore()

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 24, "normal"))



