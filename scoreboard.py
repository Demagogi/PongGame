from turtle import Turtle  # import Turtle class from turtle module


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        """updates the score on the screen"""
        self.goto(60, 200)
        self.write(arg=self.r_score, align="center", font=("arial", 50, "normal"))
        self.goto(-60, 200)
        self.write(arg=self.l_score, align="center", font=("arial", 50, "normal"))

    def l_point(self):
        """adds 1 point to the left paddle"""
        self.clear()
        self.l_score += 1
        self.update_score()

    def r_point(self):
        """adds 1 point to the right paddle"""
        self.clear()
        self.r_score += 1
        self.update_score()
