import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
player = Player()
car = CarManager(10)
screen.setup(width=600, height=600)
screen.tracer(0, 0)
screen.delay(0)

# screen.delay(0)
screen.onkeypress(player.moveForward, 'Up')

game_is_on = True
while game_is_on:
    if player.lives == 0:
        player.lives = 3
        player.level = 1
    if player.level == 10:
        player.lives = 3
        player.level = 1
    gameSpeed = str('0.0' + str(player.level))
    car.moveForward(player, player.position())
    time.sleep(0.1 - float(gameSpeed))
    screen.update()
    player.nextLevel()
    player.scorePrinter()
    player.livesPrinter()
