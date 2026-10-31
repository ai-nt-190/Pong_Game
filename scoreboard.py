from turtle import Turtle
FINAL_SCORE = 3


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 250)
        self.write(f"First to score {FINAL_SCORE}, wins", align="center", font=("Courier", 15, "normal"))
        self.goto(-200, 250)
        self.write(self.l_score, align="center", font=("Courier", 15, "normal"))
        self.goto(200, 250)
        self.write(self.r_score, align="center", font=("Courier", 15, "normal"))
        if self.r_score == FINAL_SCORE:
            self.home()
            self.write("Right player wins!!", align="center", font=("Courier", 30, "normal"))
            return True
        elif self.l_score == FINAL_SCORE:
            self.home()
            self.write("Left player wins!! ", align="center", font=("Courier", 30, "normal"))
            return True

    def l_point(self):
        self.l_score += 1
        self.clear()
        return self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        return self.update_scoreboard()
