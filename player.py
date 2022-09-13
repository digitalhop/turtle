from turtle import Turtle
import time


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        # super().__init__()
        # self.theScreen = screen
        self.thePlayer = Turtle()
        self.thePlayer.clear()
        self.thePlayer.penup()
        self.thePlayer.hideturtle()
        self.thePlayer.shape("turtle")
        self.thePlayer.setheading(90)
        self.thePlayer.setposition(0.00, -280)
        self.thePlayer.showturtle()
        self.level = 1
        self.lives = 3
        self.theScore = Turtle()
        self.theLives = Turtle()

    def position(self):
        return self.thePlayer.pos()

    def moveForward(self):
        self.thePlayer.forward(25)

    def nextLevel(self):
        if self.thePlayer.ycor() > 280:
            self.level += 1
            time.sleep(2)
            self.thePlayer.setposition(0.00, -280)

    def squashed(self):

        self.lives -= 1
        time.sleep(2)
        self.thePlayer.setposition(0.00, -280)

    def scorePrinter(self):

        self.theScore.clear()
        self.theScore.pencolor('black')
        self.theScore.penup()
        self.theScore.hideturtle()
        self.theScore.goto(-280, 250)
        self.theScore.write('Level: ' + str(self.level),
                            font=('arial', 30, 'normal'))

    def livesPrinter(self):

        self.theLives.clear()
        self.theLives.pencolor('black')
        self.theLives.penup()
        self.theLives.hideturtle()
        self.theLives.goto(0, 250)
        self.theLives.write('Shells: ' + str(self.lives),
                            font=('arial', 30, 'normal'))
