"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, additional_cargo: int):
        if self.cargo + additional_cargo > self.max_cargo:
            raise CargoOverload(f"Невозможно загрузить {additional_cargo} ед. груза. "
                                f"Будет превышена максимальная грузоподъемность в {self.max_cargo} ед.")
        self.cargo += additional_cargo

    def remove_all_cargo(self) -> int:
        cargo_before_removal = self.cargo
        self.cargo = 0
        return cargo_before_removal