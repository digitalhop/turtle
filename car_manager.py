from turtle import Turtle
from random import randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, carCount=10):
        self.carGarage = []
        self.trailorGarage = []
        for i in range(carCount):
            self.newCar()

    def newCar(self):
        self.aCar = Turtle(visible=False)
        self.aCar.hideturtle()
        self.aCar.speed(0)
        self.aCar.penup()
        self.aCar.shape("square")
        self.aCar.setheading(180)
        self.aCar.setposition(randrange(320, 900, 20),
                              randrange(-240, 260, 20))
        self.randonColourNumber = randrange(0, 5, 1)
        self.theCarColour = COLORS[self.randonColourNumber]
        self.aCar.color(self.theCarColour)
        self.aCar.shapesize(1, 2, 1)
        self.aCar.showturtle()
        self.counter = 0
        self.carGarage.append(self.aCar)

    def Trailor(self, color, xposition, yposition):
        self.bCar = Turtle(visible=False)
        self.bCar.hideturtle()
        self.bCar.speed(0)
        self.bCar.penup()
        self.bCar.shape("square")
        self.bCar.setheading(180)
        self.bCar.setposition(xposition + 20, yposition)
        self.aCar.color(color)
        self.bCar.showturtle()

    # def moveForward(self):
    #     if (self.counter % 4) == 0:
    #         self.aCar.forward(25)
    #     if self.aCar.xcor() <= -180:
    #         self.aCar.hideturtle()
    #         self.newCar()
    #     self.counter += 1

    def moveForward(self, player, playerPos=(0, 0)):
        car: Turtle
        for car in self.carGarage:
            if car.distance(playerPos) <= 20:
                player.squashed()
                break
            if car.xcor() <= -300:
                whereIsCar = self.carGarage.index(car)
                car.hideturtle()
                self.carGarage.pop(whereIsCar)
                self.newCar()
            else:
                car.forward(20)
