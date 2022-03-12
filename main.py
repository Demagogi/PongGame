# # # # # # # # # # # # #
#  giorgis pong game    #
#                       #
# # # # # # # # # # # # #
from turtle import Screen  # import Screen class from turtle module
from paddle import Paddle  # import Paddle class
from ball import Ball  # import Ball class
import time
from scoreboard import Scoreboard  # import Scoreboard class

screen = Screen()  # create object from Screen class
screen.title("My first pong")  # setup screen object
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))  # create right_paddle object from Paddle class
l_paddle = Paddle((-350, 0))  # create left_paddle object from Paddle class

ball = Ball()  # create ball object from Ball class

scoreboard = Scoreboard()  # create scoreboard object from Scoreboard class

screen.listen()

screen.onkey(r_paddle.up, "Up")  # key commands for right_paddle(right player)
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")  # key commands for left_paddle(left player)
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:  
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    # detect collision with the wall (top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    # detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
