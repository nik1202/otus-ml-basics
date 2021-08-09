from abc import ABC

import exceptions as ex

class Vehicle(ABC):

    def __init__(self, weight=100, fuel=100, fuel_consumption=10):
        self.started = False
        self.fuel = fuel
        self.weight = weight
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise ex.LowFuelError

    def move(self, distance):
        expected_fuel_amount = distance * self.fuel_consumption
        if expected_fuel_amount < self.fuel:
            self.fuel = self.fuel - expected_fuel_amount
        else:
            raise ex.NotEnoughFuel


class Engine:

    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption):
        super(Car, self).__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo):
        tmp_cargo = self.cargo + new_cargo
        if tmp_cargo < self.max_cargo:
            self.cargo = tmp_cargo
        else:
            raise ex.CargoOverload

    def remove_all_cargo(self):
        tmp_cargo = self.cargo
        self.cargo = 0
        return tmp_cargo
