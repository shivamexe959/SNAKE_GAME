from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 20, 'normal')
MSG ="GAME OVER"
class  Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score = 0 
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()
    def game_over(self):
        self.goto(0,0)
        self.write(f"{MSG}", align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score +=7
        self.clear()
        self.write(f"Score : {self.score}", align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    


        




        