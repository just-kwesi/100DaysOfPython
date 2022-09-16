from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super.__init__()
        self.color("white")
        self.speed('fastest')
        self.goto(0, 300)
        self.pensize(2.5)
        self.setheading(270)

        for i in range(1, 16):
            if i % 2 != 1:
                self.pendown()
                self.forward(30)
            else:
                self.penup()
                self.forward(30)
