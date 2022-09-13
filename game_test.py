from car_manager import *
from player import *


def test_car_colour():
    '''testing the car has a colour'''
    car = CarManager()
    assert car.theCarColour in ["red", "orange",
                                "yellow", "green", "blue", "purple"]


def test_car_direction():
    '''testing the car direction'''
    car = CarManager()
    assert car.aCar.heading() == 180


def test_car_position():
    '''testing the car is within allowed positions'''
    car = CarManager()
    assert -280 <= car.aCar.xcor() <= 900
    assert -260 <= car.aCar.ycor() <= 260


def test_player():
    '''testing the player class'''
    player = Player()


def test_score():
    '''testing we start with 3 lives'''
    player = Player()
    assert player.lives == 3
