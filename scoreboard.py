from turtle import Turtle
FONT = ("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.ht()
        self.goto(-280,250)
        self.write(f"level:{self.level}",align ="left",font=FONT)
    def update_level(self):
        self.level +=1
        self.clear()
        self.goto(-280, 250)
        self.write(f"level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="left", font=FONT)
