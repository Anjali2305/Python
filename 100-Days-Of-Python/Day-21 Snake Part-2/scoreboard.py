from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    user_score: int

    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.write(arg=f"Score : {self.user_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game over !!!!!! \n Your Score : {self.user_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.user_score += 1
        self.clear()
        self.update_board()
