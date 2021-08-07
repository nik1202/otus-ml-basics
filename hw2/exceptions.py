"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    print("LowFuelError")


class NotEnoughFuel(Exception):
    print("NotEnoughFuel")


class CargoOverload(Exception):
    print("CargoOverload")
