<<<<<<< HEAD
from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r'data.txt', 'r') as data:
            self.high_score = int(data.read())
        self.goto(x=0, y=270)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.write(f'Score = {self.score} High Score = {self.high_score}', True, align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.undo()
        self.write(f'Score = {self.score} High Score = {self.high_score}', True, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r'data.txt', 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()







=======
from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r'data.txt', 'r') as data:
            self.high_score = int(data.read())
        self.goto(x=0, y=270)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.write(f'Score = {self.score} High Score = {self.high_score}', True, align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.undo()
        self.write(f'Score = {self.score} High Score = {self.high_score}', True, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r'data.txt', 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()







>>>>>>> 177fd4d8fd0d7c9819631d465bc2c62e0b1e2092
