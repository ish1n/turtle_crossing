from turtle import Turtle

class Start(Turtle):
    def __init__(self):
        super().__init__()
       
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)


    def move_up(self):
        self.forward(10)

    def starting_line(self):
        self.goto(0,-280)

