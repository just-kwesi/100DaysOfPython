from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", 'orange', 'yellow', "green", "blue", "purple"]

for color in colors:
    tim = Turtle(shape="turtle")

screen.exitonclick()
