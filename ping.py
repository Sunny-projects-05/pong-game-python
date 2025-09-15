from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.listen()
ball=Ball()
scoreboard=Scoreboard()
# paddle1=Turtle()
# paddle1.shape("square")
# paddle1.penup()
# paddle1.color("white")
# paddle1.turtlesize(stretch_wid=5,stretch_len=1)
# paddle1.goto(350,0)
paddle1=Paddle(350,0)
paddle2=Paddle(-350,0)
screen.onkey(paddle1.move_up,"Up")
screen.onkey(paddle1.move_down,"Down")
screen.onkey(paddle2.move_up,"w")
screen.onkey(paddle2.move_down,"s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
    if ball.xcor() > 320 and ball.distance(paddle1) < 50 and ball.x_move > 0:
        ball.bounce_x()
        ball.move_speed*=0.9
    elif ball.xcor() < -320 and ball.distance(paddle2) < 50 and ball.x_move < 0:
        ball.bounce_x()
        ball.move_speed *= 0.9
    if scoreboard.l_score == 3:
        scoreboard.game_over("Left Player Wins!")
        game_is_on = False
    elif scoreboard.r_score == 3:
        scoreboard.game_over("Right Player Wins!")
        game_is_on = False

screen.exitonclick()