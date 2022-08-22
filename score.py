from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.display()

    def display(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def r_point(self):
        self.r_score += 1
        self.display()

    def l_point(self):
        self.l_score += 1
        self.display()

