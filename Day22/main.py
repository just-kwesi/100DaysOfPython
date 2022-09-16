import time
from turtle import Screen
from player import Player
from line import Line

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player1 = Player("left")
player2 = Player("right")
# line = Line()


screen.listen()
screen.onkey(player1.up,'w')
screen.onkey(player1.down,'s')
screen.onkey(player2.up,'Up')
screen.onkey(player2.down,'Down')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
