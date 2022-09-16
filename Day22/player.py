from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (0, 20), (0, 40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Player:
    def __init__(self, side):
        self.segment = []
        self.create_block()
        self.goto_side(side)

    def create_block(self):
        for position in STARTING_POSITIONS:
            seg = Turtle("square")
            seg.color('white')
            seg.penup()
            seg.goto(position)
            self.segment.append(seg)

    def move(self):
        length = len(self.segment) - 1
        for seg in range(length, 0, -1):
            x = self.segment[seg - 1].xcor()
            y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x, y)
        self.segment[0].forward(MOVE_DISTANCE)

    def goto_side(self, side):

        for seg in range(len(self.segment)):
            if side == "left":
                y = self.segment[seg].ycor()
                self.segment[seg].goto(-260, y)
            elif side == "right":
                y = self.segment[seg].ycor()
                self.segment[seg].goto(260, y)

    def up(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(UP)
        self.move()

    def down(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(DOWN)
        self.move()
