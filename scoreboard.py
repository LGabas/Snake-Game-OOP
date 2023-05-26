from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=270)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.write(f'Score = {self.score}', True, align=ALIGN, font=FONT)

    def score_up(self):
        self.score += 1
        self.undo()
        self.write(f'Score = {self.score}', True, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f'Game Over', True, align=ALIGN, font=FONT)








