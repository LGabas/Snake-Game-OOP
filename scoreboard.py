from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(x=0, y=270)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.write(f'Score = {self.score}', True, align=ALIGN, font=FONT)

    def score_up(self):
        self.score += 1
        self.undo()
        self.write(f'Score = {self.score}', True, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0









