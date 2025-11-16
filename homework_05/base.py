"""
Доработайте класс `Vehicle`
"""
from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    weight: int = 1000
    started: bool = False
    fuel: int = 0
    fuel_consumption: int = 10

    def __init__(self, weight: int, fuel: int, fuel_consumption: int):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Не хватает бензина чтобы завестись")

    def move(self, distance: int):
        fuel_required = distance * self.fuel_consumption

        if self.fuel >= fuel_required:
            self.fuel -= fuel_required
        else:
            raise NotEnoughFuel("Не хватает бензина чтобы ехать")