from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):  # paddle is a turtle aswell
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def up(self):  # order, to go up
        y = self.ycor() + 20
        self.sety(y)

    def down(self):  # order, to go down
        y = self.ycor() - 20
        self.sety(y)
