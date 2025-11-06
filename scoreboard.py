from idlelib.configdialog import FontPage
from turtle import Turtle
import snake

ALIGNMENT = "center"
FONT = ("Lucida Console", 12, "bold")
GAME_OVER_FONT = ("Lucida Console", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(arg="Score:  0", align=ALIGNMENT,
                   font=FONT)
        self.score_counter = 0

    def score_updater(self):
        self.score_counter += 1
        self.clear()
        self.write(f"Score:  {self.score_counter}",
                   align=ALIGNMENT,
                   font=FONT)

    def game_over_text(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT,
                   font=GAME_OVER_FONT)

